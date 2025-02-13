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