from web3 import Web3

MAX_UINT = 2**256 - 1
NATIVE_ADDRESS = Web3.to_checksum_address("0x0000000000000000000000000000000000000000")

FWX_MEMBERSHIP_ADDRESS_BASE = Web3.to_checksum_address("0xA273805161d0768F2B01ee065CEb36675bf5Fd86")
FWX_PERP_CORE_ADDRESS_BASE = Web3.to_checksum_address("0xaf5a41Ad65752B3CFA9c7F90a516a1f7b3ccCdeD")
FWX_PERP_HELPER_ADDRESS_BASE = Web3.to_checksum_address('0x8E8eF0aDC2D0901EA6A67B63400bBa6229F83174')

PYTH_ID:dict[str,str] = {
            "BTC": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43",
            "AVAX": "93da3352f9f1d105fdfe4971cfa80e9dd777bfc5d0f683ebb6e1294b92137bb7",
            "SOL": "ef0d8b6fda2ceba41da15d4095d1da392a0d2f8ed0c6c7bc0f4cfac8c280b56d",
            "ETH": "ff61491a931112ddf1bd8147cd1b641375f79f5825126d665480874634fd0ace",
            "DOGE": "dcef50dd0a4cd2dcc17e45df1676dcb336a11a61c69df7a0299b0150c672d25c"
            }