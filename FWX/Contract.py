from web3 import (
    Web3,
)
from web3.contract.contract import (
    Contract,
    ContractEvent,
    ContractFunction
)
from hexbytes import HexBytes
from eth_typing import (
    ChecksumAddress,
    BlockIdentifier
)
from web3.types import (
    Wei,
)
from web3.types import (
    EventData,
)

from .W3 import (
    Web3HTTP
)
from .types import (
    BaseEventData,
    TxParamsInput,
    AddressLike
)
from .Constant import(
    ERC20_ABI
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