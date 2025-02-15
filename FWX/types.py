from typing import NamedTuple, Union,Sequence,NewType
from hexbytes import HexBytes
from eth_typing import (
    Address,
    ChecksumAddress,
    HexStr,
)
from web3.types import (
    Wei,
    Nonce,
)

class AccessListEntry(NamedTuple):
    address: HexStr
    storageKeys: Sequence[HexStr]


AddressLike = Union[Address, ChecksumAddress,str]
AccessList = NewType("AccessList", Sequence[AccessListEntry])
class BaseEventData(NamedTuple):
    address: ChecksumAddress
    block_hash: HexBytes
    block_number: int
    event: str
    log_index: int
    transaction_hash: HexBytes
    transaction_index: int
    
class TxParamsInput(NamedTuple):
    accessList:AccessList|None = None
    blobVersionedHashes:Sequence[Union[str, HexStr, bytes, HexBytes]]|None = None
    chinId:int|None = None
    data:Union[bytes, HexStr]|None = None
    from_address:ChecksumAddress|None = None
    gas:int|None = None
    gasPrice:Wei|None = None
    maxFeePerBlobGas:Union[str, Wei]|None = None
    maxFeePerGas:Union[str, Wei]|None = None
    maxPriorityFeePerGas: Union[str, Wei]|None = None
    nonce: Nonce|None = None
    to:ChecksumAddress|None = None
    type:Union[int, HexStr]|None = None
    value:Wei|None = None
    
class ERC20TransferArgs(NamedTuple):
    from_address: ChecksumAddress
    to_address: ChecksumAddress
    value: int
    
class ERC20TransferEventData(BaseEventData):
    def __new__(cls, address: ChecksumAddress, block_hash: HexBytes, block_number: int, log_index: int, transaction_hash: HexBytes, transaction_index: int, args: ERC20TransferArgs) -> 'ERC20TransferEventData':
        return super().__new__(cls, address, block_hash, block_number, "Transfer", log_index, transaction_hash, transaction_index)
    
    def __init__(self, address: ChecksumAddress, block_hash: HexBytes, block_number: int, log_index: int, transaction_hash: HexBytes, transaction_index: int, args:ERC20TransferArgs) -> None:
        self.args = args
    
class FWXPerpCoreOpenPositionArgs(NamedTuple):
    owner:ChecksumAddress
    nft_id:int
    pos_id:int
    entry_price:int
    leverage:int
    contract_size:int
    is_long:bool
    pair_bytes32:bytes
    collateral_swap_amount_locked:int
    router_address:ChecksumAddress
    
class FWXPerpCoreOpenPositionEventData(BaseEventData):
    def __new__(cls, address: ChecksumAddress, block_hash: HexBytes, block_number: int, log_index: int, transaction_hash: HexBytes, transaction_index: int, args: FWXPerpCoreOpenPositionArgs) -> 'FWXPerpCoreOpenPositionEventData':
        return super().__new__(cls, address, block_hash, block_number, "OpenPosition", log_index, transaction_hash, transaction_index)
    
    def __init__(self, address: ChecksumAddress, block_hash: HexBytes, block_number: int, log_index: int, transaction_hash: HexBytes, transaction_index: int, args:FWXPerpCoreOpenPositionArgs) -> None:
        self.args = args
        
class FWXPerpCoreClosePositionArgs(NamedTuple):
    owner:ChecksumAddress
    nft_id:int
    pos_id:int
    closing_size:int
    close_price:int
    pnl:int
    is_long:bool
    close_all_position:bool
    pair_bytes32:bytes
    collateral_swap_amount_unlocked:int
    router_address:ChecksumAddress
    
class FWXPerpCoreClosePositionEventData(BaseEventData):
    def __new__(cls, address: ChecksumAddress, block_hash: HexBytes, block_number: int, log_index: int, transaction_hash: HexBytes, transaction_index: int, args: FWXPerpCoreClosePositionArgs) -> 'FWXPerpCoreClosePositionEventData':
        return super().__new__(cls, address, block_hash, block_number, "ClosePosition", log_index, transaction_hash, transaction_index)
    
    def __init__(self, address: ChecksumAddress, block_hash: HexBytes, block_number: int, log_index: int, transaction_hash: HexBytes, transaction_index: int, args:FWXPerpCoreClosePositionArgs) -> None:
        self.args = args
    
class FWXPerpHelperGetBalanceRespond(NamedTuple):
    net_balance:int
    avaliable_balance:int
    
class FWXPerpHelperGetAllPositionRespond(NamedTuple):
    pos_id:int
    is_long:bool
    collateral_address:ChecksumAddress
    underlying_address:ChecksumAddress
    entry_price:int
    current_price:int
    contract_size:int
    collateral_swapped_amount:int
    liquidation_price:int
    pnl:int
    roe:int
    margin:int
    leverage:int
    tp_price:int
    sl_price:int
    
class FWXPerpCoreGetPositionRespond(NamedTuple):
    pos_id:int
    last_settle_timestamp:int
    collateral_address:ChecksumAddress
    underlying_address:ChecksumAddress
    entry_price:int
    contract_size:int
    collateral_locked:int
    leverage:int