from web3 import (
    Web3,
    HTTPProvider
)
from web3.middleware.proof_of_authority import (
    ExtraDataToPOAMiddleware
    )

from hexbytes import HexBytes
import asyncio
from typing import (
    Any,
    Optional,  
    Dict)
from eth_typing import (
    ChecksumAddress,
    BlockIdentifier
)
from web3.contract.contract import (
    Contract,
    ContractEvent,
)
from web3.contract.async_contract import (
    
    AsyncContract,
    AsyncContractEvent
)
from web3.types import (
    EventData,
    TxReceipt,
    TxParams,
    Wei,
    Nonce,
)
from web3._utils.events import (
    EventLogErrorFlags,
)
from eth_account.datastructures import (
    SignedTransaction,
)

from eth_account.signers.local import (
    LocalAccount,
)

from .types import (
    BaseEventData,
    TxParamsInput
)

class Web3HTTP:
    
    def __init__(self, provider:str) -> None:
        self.w3 = Web3(HTTPProvider(provider))
        self.chain_id = self.w3.eth.chain_id
        if self.chain_id == 43113:
            self.w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)
            
    def load_contract(self,abi:Any,address:ChecksumAddress) -> Contract:
        return self.w3.eth.contract(abi=abi,address=address) 
    
    def get_event_data_with_txn(self,
                                txn:HexBytes,
                                event:ContractEvent,
                                error:EventLogErrorFlags=EventLogErrorFlags.Discard) -> tuple[EventData]:
        
        receipt = self.w3.eth.get_transaction_receipt(txn)
        return event.process_receipt(receipt,errors=error)
    
    def get_event_data_with_block(self,
                                  event:ContractEvent,
                                  argument_filters: Optional[Dict[str, Any]] = None,
                                  from_block: Optional[BlockIdentifier] = None,
                                  to_block: Optional[BlockIdentifier] = None)->tuple[EventData]:
        
        return event.get_logs(from_block=from_block, to_block=to_block, argument_filters=argument_filters)
    
    def process_event_data(self, event_data:EventData) -> tuple[BaseEventData, dict[str, Any]]:
        address: ChecksumAddress = Web3.to_checksum_address(event_data['address'])
        blockHash: HexBytes = HexBytes(event_data['blockHash'])
        blockNumber: int = int(event_data['blockNumber'])
        logIndex: int = int(event_data['logIndex'])
        transactionHash: HexBytes = HexBytes(event_data['transactionHash'])
        transactionIndex: int = int(event_data['transactionIndex'])
        event_name = event_data['event']
        args = event_data['args']
        return BaseEventData(address,blockHash,blockNumber,event_name,logIndex,transactionHash,transactionIndex),args 
    
class Web3WalletHTTP(Web3HTTP):
    
    def __init__(self, 
                 provider:str, 
                 private_key:str) -> None:
        super().__init__(provider)
        self.__private_key = private_key
        account:LocalAccount = self.w3.eth.account.from_key(private_key)
        self.wallet_address:ChecksumAddress = account.address
        self.last_nonce:Nonce|None = None
        pass 
    
    def create_txn_params(self, tx_params:TxParamsInput=TxParamsInput()) -> TxParams:
        txn_params:TxParams = {'from':self.wallet_address,
                               'chainId':self.chain_id}
        
        for key, value in tx_params._asdict().items():
            if value is not None:
                txn_params[key] = value
                
        if 'nonce' not in txn_params:
            if self.last_nonce is None:
                self.last_nonce = Nonce(0)
            nonce:Nonce = max(self.last_nonce, self.w3.eth.get_transaction_count(self.wallet_address))
            txn_params['nonce'] = nonce
            
        return txn_params
    
    def checking_txn_params(self, txn_params:TxParams) -> TxParams:
        if 'nonce' not in txn_params:
            if self.last_nonce is None:
                self.last_nonce = Nonce(0)
            nonce:Nonce = max(self.last_nonce, self.w3.eth.get_transaction_count(self.wallet_address))
            txn_params['nonce'] = nonce
            
        if 'to' not in txn_params:
            raise ValueError("Destination address is required")  
            
        return txn_params
    
    def create_txn_params_with_func(self,
                                    func)
    
    