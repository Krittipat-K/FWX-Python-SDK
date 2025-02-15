from typing import (
    Optional,
)
from web3 import (
    Web3,
)
from web3.contract.contract import (
    ContractEvent,
    ContractFunction
)
from eth_typing import (
    ChecksumAddress,
)
from web3.types import (
    Wei,
)
from web3.types import (
    EventData,
)

from .W3 import (
    Web3HTTP,
    Web3WalletHTTP
)
from .types import (
    AddressLike,
    ERC20TransferArgs,
    ERC20TransferEventData,
    FWXPerpCoreGetPositionRespond,
    FWXPerpCoreOpenPositionArgs,
    FWXPerpCoreOpenPositionEventData,
    FWXPerpCoreClosePositionArgs,
    FWXPerpCoreClosePositionEventData,
    FWXPerpHelperGetAllPositionRespond,
    FWXPerpHelperGetBalanceRespond
)
from .Constant import(
    ERC20_ABI,
    FWX_MEMBERSHIP_ABI,
    FWX_MEMBERSHIP_ADDRESS_BASE,
    FWX_PERP_CORE_ABI,
    FWX_PERP_CORE_ADDRESS_BASE,
    FWX_PERP_HELPER_ABI,
    FWX_PERP_HELPER_ADDRESS_BASE,
    MAX_UINT
)

class ERC20ContractBase(Web3HTTP):
    
    def __init__(self, 
                 provider: str,
                 address:AddressLike) -> None:
        super().__init__(provider)
        self.address = Web3.to_checksum_address(address)
        self.contract = self.load_contract(ERC20_ABI,self.address)
        
        # Call Function Section
        
    def balanceOf(self,address:ChecksumAddress) -> ContractFunction:
    
        return self.contract.functions.balanceOf(address)
    
    def allowance(self,owner:ChecksumAddress,spender:ChecksumAddress) -> ContractFunction:
        
        return self.contract.functions.allowance(owner,spender)
    
    def name(self) -> ContractFunction:
        
        return self.contract.functions.name()
    
    def totalSupply(self) -> ContractFunction:
        
        return self.contract.functions.totalSupply()
    
    def symbol(self) -> ContractFunction:
        
        return self.contract.functions.symbol()
    
    def decimals(self) -> ContractFunction:
        
        return self.contract.functions.decimals()
    
    # Transaction Section
    
    def approve(self,spender:ChecksumAddress,amount:Wei,) -> ContractFunction:
        
        return self.contract.functions.approve(spender,amount)
    
    def transfer(self,to:ChecksumAddress,amount:Wei) -> ContractFunction:
        
        return self.contract.functions.transfer(to,amount)
    
    def transferFrom(self,from_:ChecksumAddress,to:ChecksumAddress,amount:Wei) -> ContractFunction:
        
        return self.contract.functions.transferFrom(from_,to,amount)
    
    # Event Section
    
    def Transfer(self) -> ContractEvent:
        
        return self.contract.events.Transfer()
    
class ERC20Contract(ERC20ContractBase):
    
    def __init__(self, 
                 provider: str,
                 address:AddressLike) -> None:
        super().__init__(provider,address)
        self.token_symbol = self.get_symbol()
        self.decimal = self.get_decimals()
        
    def get_balanceOf(self,address:ChecksumAddress) -> Wei:
        
        return self.balanceOf(address).call()
    
    def get_allowance(self,owner:ChecksumAddress,spender:ChecksumAddress) -> Wei:
        
        return self.allowance(owner,spender).call()
    
    def get_name(self) -> str:
        
        return self.name().call()
    
    def get_totalSupply(self) -> Wei:
        
        return self.totalSupply().call()
    
    def get_symbol(self) -> str:
        
        return self.symbol().call()
    
    def get_decimals(self) -> int:
        
        return self.decimals().call()
    
    def process_transfer_event(self,event:EventData) -> ERC20TransferEventData:
        
        base_event_data,arg = self.process_event_data(event)
        sender = Web3.to_checksum_address(arg['from'])
        receiver = Web3.to_checksum_address(arg['to'])
        value = int(arg['value'])
        transfer_args = ERC20TransferArgs(sender,receiver,value)
        return ERC20TransferEventData(address=base_event_data.address,
                                       block_hash=base_event_data.block_hash,
                                       block_number=base_event_data.block_number,
                                       transaction_hash=base_event_data.transaction_hash,
                                       log_index=base_event_data.log_index,
                                       transaction_index=base_event_data.transaction_index,
                                       args=transfer_args)
    def check_approval(self,
                       wallet:Web3WalletHTTP,
                       spender:ChecksumAddress,
                       amount:int=MAX_UINT,) -> int:
        
        owner = wallet.wallet_address
        allowance:int = self.get_allowance(owner,spender)
        if allowance < amount:
            print(f'Approve {amount} to {spender} from {owner}')
            func = self.approve(spender,Wei(amount))
            txn = wallet.build_and_send_transaction(func)
            wallet.w3.eth.wait_for_transaction_receipt(txn)
            return amount
        
        else:
            return allowance
class FWXMembershipContractBase(Web3HTTP):
    
    def __init__(self, 
                 provider: str,
                 address:Optional[AddressLike]=None) -> None:
        super().__init__(provider)
        if address is None:
            match self.chain_id:
                case 8453:
                    self.address = FWX_MEMBERSHIP_ADDRESS_BASE
                case _:
                    raise ValueError("Invalid Chain ID")
        else:
            self.address = Web3.to_checksum_address(address)
            
        self.contract = self.load_contract(FWX_MEMBERSHIP_ABI,self.address)
        
        # Call Function Section
        
    def getDefaultMembership(self,wallet_address:ChecksumAddress) -> ContractFunction:
    
        return self.contract.functions.getDefaultMembership(wallet_address)
    
    
    # Transaction Section
    
    def mint(self,reffeal_id:int) -> ContractFunction:
        
        return self.contract.functions.mint(reffeal_id)
    
class FWXMembershipContract(FWXMembershipContractBase):
    
    def __init__(self, 
                 provider: str,
                 address:Optional[AddressLike]=None) -> None:
        super().__init__(provider,address)
        
    def get_default_membership(self,wallet_address:ChecksumAddress) -> int:
        
        return self.getDefaultMembership(wallet_address).call()
    
class FWXPerpCoreContractBase(Web3HTTP):
    
    def __init__(self, 
                 provider: str,
                 address:Optional[AddressLike]=None) -> None:
        super().__init__(provider)
        if address is None:
            match self.chain_id:
                case 8453:
                    self.address = FWX_PERP_CORE_ADDRESS_BASE
                case _:
                    raise ValueError("Invalid Chain ID")
        else:
            self.address = Web3.to_checksum_address(address)
            
        self.contract = self.load_contract(FWX_PERP_CORE_ABI,self.address)
        
    # Call function Section
    
    def getPosition(self,
                    nft_id:int,
                    underlying_address:ChecksumAddress)->ContractFunction:
        
        return self.contract.functions.getPosition(nft_id,underlying_address)
    
    # Transaction Section
    
    def depositCollateral(self,
                          nft_id:int,
                          collateral_address:ChecksumAddress,
                          underlying_address:ChecksumAddress,
                          amount:int)->ContractFunction:
        
        return self.contract.functions.depositCollateral(nft_id,collateral_address,underlying_address,amount)
    
    def withdrawCollateral(self,
                           nft_id:int,
                           collateral_address:ChecksumAddress,
                           underlying_address:ChecksumAddress,
                           amount:int,
                           pyth_update_data:list[bytes])->ContractFunction:
        
        return self.contract.functions.withdrawCollateral(nft_id,collateral_address,underlying_address,amount,pyth_update_data)
    
    def openPosition(self,
                     nft_id:int,
                     is_long:bool,
                     collateral_address:ChecksumAddress,
                     underlying_address:ChecksumAddress,
                     contract_size_in_collateral:int,
                     leverage:int,
                     pyth_update_data:list[bytes])->ContractFunction:
        
        return self.contract.functions.openPosition(nft_id,is_long,collateral_address,underlying_address,contract_size_in_collateral,leverage,pyth_update_data)
    
    def closePosition(self,
                      nft_id:int,
                      position_id:int,
                      closing_size:int,
                      pyth_update_data:list[bytes])->ContractFunction:
        
        return self.contract.functions.closePosition(nft_id,position_id,closing_size,pyth_update_data)
    
    def closeAllPositions(self,
                          nft_id:int,
                          pyth_update_data:list[bytes])->ContractFunction:
        
        return self.contract.functions.closeAllPositions(nft_id,pyth_update_data)
    
    # Event Section
    
    def eventOpenPosition(self) -> ContractEvent:
        
        return self.contract.events.OpenPosition()
    
    def eventClosePosition(self) -> ContractEvent:
        
        return self.contract.events.ClosePosition()

class FWXPerpCoreContract(FWXPerpCoreContractBase):
    
    def __init__(self, 
                 provider: str,
                 address:Optional[AddressLike]=None) -> None:
        super().__init__(provider,address)
        
    def get_position(self,nft_id:int,underlying_address:ChecksumAddress) -> FWXPerpCoreGetPositionRespond:
        
        res = self.getPosition(nft_id,underlying_address).call()
        
        return FWXPerpCoreGetPositionRespond(*res)
    
    def deposit_collateral(self,
                            nft_id:int,
                            collateral_address:ChecksumAddress,
                            underlying_address:ChecksumAddress,
                            amount:int) -> ContractFunction:
        
        return self.depositCollateral(nft_id,
                                      collateral_address,
                                      underlying_address,
                                      amount)
        
    def withdraw_collateral(self,
                            nft_id:int,
                            collateral_address:ChecksumAddress,
                            underlying_address:ChecksumAddress,
                            amount:int,
                            pyth_update_data:list[bytes]) -> ContractFunction:
        
        return self.withdrawCollateral(nft_id,
                                       collateral_address,
                                       underlying_address,
                                       amount,
                                       pyth_update_data)
        
    def open_position(self,
                        nft_id:int,
                        is_long:bool,
                        collateral_address:ChecksumAddress,
                        underlying_address:ChecksumAddress,
                        contract_size_in_collateral:int,
                        leverage:int,
                        pyth_update_data:list[bytes]) -> ContractFunction:
        
        return self.openPosition(nft_id,
                                is_long,
                                collateral_address,
                                underlying_address,
                                contract_size_in_collateral,
                                leverage,
                                pyth_update_data)
        
    def close_position(self,
                        nft_id:int,
                        position_id:int,
                        closing_size:int,
                        pyth_update_data:list[bytes]) -> ContractFunction:
        
        return self.closePosition(nft_id,
                                 position_id,
                                 closing_size,
                                 pyth_update_data)
        
    def close_all_positions(self,
                            nft_id:int,
                            pyth_update_data:list[bytes]) -> ContractFunction:
        
        return self.closeAllPositions(nft_id,
                                     pyth_update_data)
        
    
    def process_open_position_event(self,event:EventData) -> FWXPerpCoreOpenPositionEventData:
            
        base_event_data,arg = self.process_event_data(event)
        owener = Web3.to_checksum_address(arg['owner'])
        nft_id = int(arg['nftId'])
        position_id = int(arg['posId'])
        entry_price = int(arg['entryPrice'])
        leverage = int(arg['leverage'])
        contract_size = int(arg['contractSize'])
        is_long = arg['isLong']
        pair_bytes = arg['pairByte']
        collateral_swap_amount_locked = int(arg['collateralSwappedAmountLock'])
        router_address = Web3.to_checksum_address(arg['router'])
        
        return FWXPerpCoreOpenPositionEventData(address=base_event_data.address,
                                                block_hash=base_event_data.block_hash,
                                                block_number=base_event_data.block_number,
                                                transaction_hash=base_event_data.transaction_hash,
                                                log_index=base_event_data.log_index,
                                                transaction_index=base_event_data.transaction_index,
                                                args=FWXPerpCoreOpenPositionArgs(owener,nft_id,position_id,entry_price,leverage,contract_size,is_long,pair_bytes,collateral_swap_amount_locked,router_address))
        
    def get_process_close_position_event_log(self,event_log:EventData) -> FWXPerpCoreClosePositionEventData:
        base_event_data,arg = self.process_event_data(event_log)
        owener = Web3.to_checksum_address(arg['owner'])
        nft_id = int(arg['nftId'])
        position_id = int(arg['posId'])
        closing_size = int(arg['closingSize'])
        closing_price = int(arg['closingPrice'])
        pnl = int(arg['pnl'])
        is_long = arg['isLong']
        clooe_all_positions = arg['closeAllPosition']
        pair_bytes = arg['pairByte']
        collateral_swap_amount_unlocked = int(arg['collateralSwappedAmountUnlock'])
        router_address = Web3.to_checksum_address(arg['router'])
        
        return FWXPerpCoreClosePositionEventData(address=base_event_data.address,
                                                block_hash=base_event_data.block_hash,
                                                block_number=base_event_data.block_number,
                                                transaction_hash=base_event_data.transaction_hash,
                                                log_index=base_event_data.log_index,
                                                transaction_index=base_event_data.transaction_index,
                                                args=FWXPerpCoreClosePositionArgs(owener,nft_id,position_id,closing_size,closing_price,pnl,is_long,clooe_all_positions,pair_bytes,collateral_swap_amount_unlocked,router_address))
        
class FWXPerpHelperContractBase(Web3HTTP):
    
    def __init__(self,
                    provider:str,
                    address:Optional[AddressLike]=None) -> None:
            super().__init__(provider)
            if address is None:
                match self.chain_id:
                    case 8453:
                        self.address = FWX_PERP_HELPER_ADDRESS_BASE
                    case _:
                        raise ValueError("Invalid Chain ID")
            else:
                self.address = Web3.to_checksum_address(address)
                
            self.contract = self.load_contract(FWX_PERP_HELPER_ABI,self.address)
            
    # Call function Section
    
    def getMaxContractSize(self,
                           perps_core_address:ChecksumAddress,
                           nft_id:int,
                           underlying_address:ChecksumAddress,
                           is_new_long:bool,
                           leverage:int,
                           safety_factor:int,
                           pyth_data:list[tuple[bytes,tuple[int,...],tuple[int,...]]])->ContractFunction:
        
        return self.contract.functions.getMaxContractSize(perps_core_address,nft_id,underlying_address,is_new_long,leverage,safety_factor,pyth_data)
    
    def getBalance(self,
                   perps_core_address:ChecksumAddress,
                   nft_id:int,
                   pyth_data:list[tuple[bytes,tuple[int,...],tuple[int,...]]])->ContractFunction:
        
        return self.contract.functions.getBalance(perps_core_address,nft_id,pyth_data)
    
    def getAllActivePositions(self,
                              perps_core_address:ChecksumAddress,
                              nft_id:int,
                              pyth_data:list[tuple[bytes,tuple[int,...],tuple[int,...]]])->ContractFunction:
        
        return self.contract.functions.getAllActivePositions(perps_core_address,nft_id,pyth_data)
    
class FWXPerpHelperContract(FWXPerpHelperContractBase):
    
    def __init__(self,
                    provider:str,
                    address:Optional[AddressLike]=None) -> None:
        super().__init__(provider,address)
        
    def get_max_contract_size(self,
                              perps_core_address:ChecksumAddress,
                              nft_id:int,
                              underlying_address:ChecksumAddress,
                              is_new_long:bool,
                              leverage:int,
                              safety_factor:int,
                              pyth_data:list[tuple[bytes,tuple[int,...],tuple[int,...]]]) -> int:
        
        return self.getMaxContractSize(perps_core_address,nft_id,underlying_address,is_new_long,leverage,safety_factor,pyth_data).call()
    
    def get_balance(self,
                    perps_core_address:ChecksumAddress,
                    nft_id:int,
                    pyth_data:list[tuple[bytes,tuple[int,...],tuple[int,...]]]) -> FWXPerpHelperGetBalanceRespond:
        
        res = self.getBalance(perps_core_address,nft_id,pyth_data).call()
        
        return FWXPerpHelperGetBalanceRespond(*res)
    
    def get_all_active_positions(self,
                                 perps_core_address:ChecksumAddress,
                                 nft_id:int,
                                 pyth_data:list[tuple[bytes,tuple[int,...],tuple[int,...]]]) -> list[FWXPerpHelperGetAllPositionRespond]|None:
        
        res = self.getAllActivePositions(perps_core_address,nft_id,pyth_data).call()
        result:list[FWXPerpHelperGetAllPositionRespond] = []
        for pos in res:
            if len(pos) > 0:
                result.append(FWXPerpHelperGetAllPositionRespond(*pos))
                
        if len(result) == 0:
            return None
        
        return result