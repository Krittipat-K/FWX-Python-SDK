from web3 import Web3
from typing import Any

MAX_UINT = 2**256 - 1
NATIVE_ADDRESS = Web3.to_checksum_address("0x0000000000000000000000000000000000000000")

FWX_MEMBERSHIP_ADDRESS_BASE = Web3.to_checksum_address("0xA273805161d0768F2B01ee065CEb36675bf5Fd86")
FWX_PERP_CORE_ADDRESS_BASE = Web3.to_checksum_address("0xaf5a41Ad65752B3CFA9c7F90a516a1f7b3ccCdeD")
FWX_PERP_HELPER_ADDRESS_BASE = Web3.to_checksum_address('0x8E8eF0aDC2D0901EA6A67B63400bBa6229F83174')

USDC_BASE = Web3.to_checksum_address("0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913")
USDC_AVALANCHE = Web3.to_checksum_address("0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e")

PYTH_ID:dict[str,str] = {
            "BTC": "e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43",
            "AVAX": "93da3352f9f1d105fdfe4971cfa80e9dd777bfc5d0f683ebb6e1294b92137bb7",
            "SOL": "ef0d8b6fda2ceba41da15d4095d1da392a0d2f8ed0c6c7bc0f4cfac8c280b56d",
            "ETH": "ff61491a931112ddf1bd8147cd1b641375f79f5825126d665480874634fd0ace",
            "DOGE": "dcef50dd0a4cd2dcc17e45df1676dcb336a11a61c69df7a0299b0150c672d25c"
            }

ERC20_ABI:list[dict[str,Any]] = [
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_spender",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_from",
                "type": "address"
            },
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [
            {
                "name": "",
                "type": "uint8"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "name": "balance",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [
            {
                "name": "",
                "type": "string"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "name": "_to",
                "type": "address"
            },
            {
                "name": "_value",
                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "name": "",
                "type": "bool"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [
            {
                "name": "_owner",
                "type": "address"
            },
            {
                "name": "_spender",
                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "payable": True,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "owner",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "spender",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "name": "from",
                "type": "address"
            },
            {
                "indexed": True,
                "name": "to",
                "type": "address"
            },
            {
                "indexed": False,
                "name": "value",
                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    }
]

FWX_MEMBERSHIP_ABI: list[dict[str,Any]] = [
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "approved",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "Approval",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "operator",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "approved",
          "type": "bool"
        }
      ],
      "name": "ApprovalForAll",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "Transfer",
      "type": "event"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "approve",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        }
      ],
      "name": "balanceOf",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "balance",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "currentPool",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "getApproved",
      "outputs": [
        {
          "internalType": "address",
          "name": "operator",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        }
      ],
      "name": "getDefaultMembership",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getPoolLists",
      "outputs": [
        {
          "internalType": "address[]",
          "name": "",
          "type": "address[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getPreviousPool",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "getRank",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "pool",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "getRank",
      "outputs": [
        {
          "internalType": "uint8",
          "name": "",
          "type": "uint8"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "getReferrer",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "operator",
          "type": "address"
        }
      ],
      "name": "isApprovedForAll",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "referalId",
          "type": "uint256"
        }
      ],
      "name": "mint",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "name": "ownerOf",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "safeTransferFrom",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "internalType": "bytes",
          "name": "data",
          "type": "bytes"
        }
      ],
      "name": "safeTransferFrom",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "operator",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "_approved",
          "type": "bool"
        }
      ],
      "name": "setApprovalForAll",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "string",
          "name": "baseTokenURI",
          "type": "string"
        }
      ],
      "name": "setBaseURI",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "setDefaultMembership",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "newPool",
          "type": "address"
        }
      ],
      "name": "setNewPool",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes4",
          "name": "interfaceId",
          "type": "bytes4"
        }
      ],
      "name": "supportsInterface",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "index",
          "type": "uint256"
        }
      ],
      "name": "tokenByIndex",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "index",
          "type": "uint256"
        }
      ],
      "name": "tokenOfOwnerByIndex",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "from",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "transferFrom",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "unpause",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        },
        {
          "internalType": "uint8",
          "name": "newRank",
          "type": "uint8"
        }
      ],
      "name": "updateRank",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "tokenId",
          "type": "uint256"
        }
      ],
      "name": "usableTokenId",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]

FWX_PERP_CORE_ABI:list[dict[str,Any]] = [
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "oldRank",
          "type": "uint8"
        },
        {
          "indexed": False,
          "internalType": "uint8",
          "name": "newRank",
          "type": "uint8"
        }
      ],
      "name": "ActivateRank",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "burner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "name": "BurnAtpToken",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "burner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "BurnPToken",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "interestTokenClaimed",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "interestTokenBonus",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "burnedItp",
          "type": "uint256"
        }
      ],
      "name": "ClaimTokenInterest",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "closingSize",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "closingPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "int128",
          "name": "pnl",
          "type": "int128"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "closeAllPosition",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "pairByte",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "collateralSwappedAmountUnlock",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "router",
          "type": "address"
        }
      ],
      "name": "ClosePosition",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "pairByte",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "uint128",
          "name": "tradingFee",
          "type": "uint128"
        },
        {
          "indexed": False,
          "internalType": "uint128",
          "name": "swapFee",
          "type": "uint128"
        },
        {
          "indexed": False,
          "internalType": "uint128",
          "name": "interestPaid",
          "type": "uint128"
        },
        {
          "indexed": False,
          "internalType": "uint128",
          "name": "liquidationFee",
          "type": "uint128"
        },
        {
          "indexed": False,
          "internalType": "uint128",
          "name": "bountyFeeToProtocol",
          "type": "uint128"
        },
        {
          "indexed": False,
          "internalType": "uint128",
          "name": "bountyFeeToLiquidator",
          "type": "uint128"
        }
      ],
      "name": "CollectFees",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "depositAmount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "mintedP",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "mintedAtp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "mintedItp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "mintedIfp",
          "type": "uint256"
        }
      ],
      "name": "Deposit",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "collateralToken",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "pairByte",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "DepositCollateral",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "liquidator",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "liquidatedSize",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "swapPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "pairByte",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "router",
          "type": "address"
        }
      ],
      "name": "LiquidatePosition",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "minter",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "name": "MintAtpToken",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "minter",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "MintPToken",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "entryPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "leverage",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "contractSize",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "pairByte",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "collateralSwappedAmountLock",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "router",
          "type": "address"
        }
      ],
      "name": "OpenPosition",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "setAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "bool",
          "name": "isAllow",
          "type": "bool"
        }
      ],
      "name": "SetAllowUnderlying",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "SetBountyFeeRateToLiquidator",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "SetBountyFeeRateToProtocol",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "SetFeeToProtocolRate",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "SetLiquidatePnlRatio",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "SetLiquidityRatio",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "SetMaintenanceMarginRatio",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "int256",
          "name": "oldValue",
          "type": "int256"
        },
        {
          "indexed": False,
          "internalType": "int256",
          "name": "newValue",
          "type": "int256"
        }
      ],
      "name": "SetMaxPnls",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "SetMaximumOpenSize",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "SetMinimumMarginRatio",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "SetMinimumOpenSize",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "tokenAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256[]",
          "name": "fundingNetOI",
          "type": "uint256[]"
        },
        {
          "indexed": False,
          "internalType": "uint256[]",
          "name": "fundingRates",
          "type": "uint256[]"
        },
        {
          "indexed": False,
          "internalType": "uint256[]",
          "name": "spreadNotional",
          "type": "uint256[]"
        },
        {
          "indexed": False,
          "internalType": "uint256[]",
          "name": "spread",
          "type": "uint256[]"
        }
      ],
      "name": "SetOIConfig",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "setter",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "oldAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "newAddress",
          "type": "address"
        }
      ],
      "name": "SetPerpCloseTrading",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "setter",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "oldAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "newAddress",
          "type": "address"
        }
      ],
      "name": "SetPerpLending",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "setter",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "oldAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "newAddress",
          "type": "address"
        }
      ],
      "name": "SetPerpTrading",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "setter",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "oldAddress",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "newAddress",
          "type": "address"
        }
      ],
      "name": "SetPerpWalletTrading",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "setter",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "oldId",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "newId",
          "type": "bytes32"
        }
      ],
      "name": "SetPythId",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "period",
          "type": "uint256"
        }
      ],
      "name": "SetStalePeriod",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "tpPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "slPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "currentPrice",
          "type": "uint256"
        }
      ],
      "name": "SetTPSL",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "SetTPSLExecutionFee",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldFee",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newFee",
          "type": "uint256"
        }
      ],
      "name": "SetTradingFee",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "trigPrice",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "closePrice",
          "type": "uint256"
        }
      ],
      "name": "TriggerTPSL",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "sender",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "totalContractSizeLong",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "totalContractSizeShort",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "averagePriceLong",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "averagePriceShort",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "int256",
          "name": "realizedLongPNL",
          "type": "int256"
        },
        {
          "indexed": False,
          "internalType": "int256",
          "name": "realizedShortPNL",
          "type": "int256"
        },
        {
          "indexed": False,
          "internalType": "int256",
          "name": "unsettleLongPNL",
          "type": "int256"
        },
        {
          "indexed": False,
          "internalType": "int256",
          "name": "unsettleShortPNL",
          "type": "int256"
        }
      ],
      "name": "UpdateGlobalStat",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "pairByte",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "oldValue",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "UpdateWallet",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "withdrawAmount",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "burnedP",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "burnedAtp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "burnedLoss",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "burnedItp",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "burnedIfp",
          "type": "uint256"
        }
      ],
      "name": "Withdraw",
      "type": "event"
    },
    {
      "anonymous": False,
      "inputs": [
        {
          "indexed": True,
          "internalType": "address",
          "name": "owner",
          "type": "address"
        },
        {
          "indexed": True,
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "collateralToken",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "indexed": False,
          "internalType": "bytes32",
          "name": "pairByte",
          "type": "bytes32"
        },
        {
          "indexed": False,
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "WithdrawCollateral",
      "type": "event"
    },
    {
      "inputs": [],
      "name": "atpTokenTotalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "balance",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "bountyFeeRateToLiquidator",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "bountyFeeRateToProtocol",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "closeAllPositions",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "closingSize",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "closePosition",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        }
      ],
      "name": "currentPositionIndex",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "depositAmount",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "deposit",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "collateralToken",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "depositCollateral",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "token",
          "type": "address"
        }
      ],
      "name": "dummyPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "feeToProtocolRate",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getAllUnRealizedPNL",
      "outputs": [
        {
          "internalType": "int256",
          "name": "result",
          "type": "int256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getAllowPythList",
      "outputs": [
        {
          "internalType": "bytes32[]",
          "name": "",
          "type": "bytes32[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getAllowUnderlyingList",
      "outputs": [
        {
          "internalType": "address[]",
          "name": "",
          "type": "address[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        }
      ],
      "name": "getBalance",
      "outputs": [
        {
          "internalType": "int256",
          "name": "netBalance",
          "type": "int256"
        },
        {
          "internalType": "uint256",
          "name": "availableBalance",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "contractSize",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        }
      ],
      "name": "getFundingFee",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "fundingFee",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "tokenAddress",
          "type": "address"
        }
      ],
      "name": "getFundingNetOI",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "contractSize",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        }
      ],
      "name": "getFundingRate",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "fundingRate",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "tokenAddress",
          "type": "address"
        }
      ],
      "name": "getFundingRates",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getInterestTokenPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        }
      ],
      "name": "getPosition",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint64",
              "name": "id",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "lastSettleTimestamp",
              "type": "uint64"
            },
            {
              "internalType": "address",
              "name": "collateralToken",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "underlyingToken",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "entryPrice",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "contractSize",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "collateralLocked",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "leverage",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpCoreBase.Position",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "tokenAddress",
          "type": "address"
        }
      ],
      "name": "getSpread",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "tokenAddress",
          "type": "address"
        }
      ],
      "name": "getSpreadNotional",
      "outputs": [
        {
          "internalType": "uint256[]",
          "name": "",
          "type": "uint256[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getTotalOI",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "totalOILong",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "totalOIShort",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        }
      ],
      "name": "getUnrealizedPnlAndFee",
      "outputs": [
        {
          "internalType": "int256",
          "name": "unrealizedPnl",
          "type": "int256"
        },
        {
          "internalType": "uint256",
          "name": "tradingFee",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "fundingFee",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingAddress",
          "type": "address"
        }
      ],
      "name": "getUnrealizedPnlAndFeeByToken",
      "outputs": [
        {
          "internalType": "int256",
          "name": "unrealizedPnl",
          "type": "int256"
        },
        {
          "internalType": "uint256",
          "name": "tradingFee",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "fundingFee",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        }
      ],
      "name": "getWallets",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        }
      ],
      "name": "globalStats",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "totalContractSizeLong",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "totalContractSizeShort",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "averagePriceLong",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "averagePriceShort",
              "type": "uint256"
            },
            {
              "internalType": "int256",
              "name": "realizedLongPNL",
              "type": "int256"
            },
            {
              "internalType": "int256",
              "name": "realizedShortPNL",
              "type": "int256"
            },
            {
              "internalType": "int256",
              "name": "settleLongPNL",
              "type": "int256"
            },
            {
              "internalType": "int256",
              "name": "settleShortPNL",
              "type": "int256"
            }
          ],
          "internalType": "struct IPerpCoreBase.GlobalStat",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        }
      ],
      "name": "isLiquidable",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "collateral",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        }
      ],
      "name": "isPythOracleIdSet",
      "outputs": [
        {
          "internalType": "bool",
          "name": "",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "liquidatePnlRatio",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "liquidatePosition",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "liquidatePositionByPositionPnl",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "liquidatePositionByTotalPnl",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "liquidity",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "liquidityRatio",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        }
      ],
      "name": "maintenanceMarginRatio",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        }
      ],
      "name": "maxPnls",
      "outputs": [
        {
          "internalType": "int256",
          "name": "",
          "type": "int256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        }
      ],
      "name": "maximumOpenSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "membershipAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        }
      ],
      "name": "minimumMarginRatio",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        }
      ],
      "name": "minimumOpenSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        }
      ],
      "name": "nftStats",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "totalCollateralLocked",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "totalMaintenanceMargin",
              "type": "uint256"
            },
            {
              "internalType": "int256",
              "name": "unsettlePnl",
              "type": "int256"
            }
          ],
          "internalType": "struct IPerpCoreBase.NftStat",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        },
        {
          "internalType": "address",
          "name": "collateralTokenAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "underlyingTokenAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "contractSize",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "leverage",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "openPosition",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        },
        {
          "internalType": "address",
          "name": "collateralToken",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "contractSize",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "leverage",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "tpPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "slPrice",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "openPositionWithTPSL",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "pTokenTotalSupply",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "balance",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "perpCloseTradingAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "perpLendingAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "perpTradingAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "perpWalletTradingAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "_currentIndex",
          "type": "uint256"
        }
      ],
      "name": "positionStates",
      "outputs": [
        {
          "components": [
            {
              "internalType": "bool",
              "name": "active",
              "type": "bool"
            },
            {
              "internalType": "bool",
              "name": "isLong",
              "type": "bool"
            },
            {
              "internalType": "int256",
              "name": "PNL",
              "type": "int256"
            },
            {
              "internalType": "uint64",
              "name": "startTimestamp",
              "type": "uint64"
            },
            {
              "internalType": "bytes32",
              "name": "pairByte",
              "type": "bytes32"
            },
            {
              "internalType": "uint256",
              "name": "totalTradingFee",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "totalFundingFee",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpCoreBase.PositionState",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "bytes32",
          "name": "pairByte",
          "type": "bytes32"
        }
      ],
      "name": "positions",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint64",
              "name": "id",
              "type": "uint64"
            },
            {
              "internalType": "uint64",
              "name": "lastSettleTimestamp",
              "type": "uint64"
            },
            {
              "internalType": "address",
              "name": "collateralToken",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "underlyingToken",
              "type": "address"
            },
            {
              "internalType": "uint256",
              "name": "entryPrice",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "contractSize",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "collateralLocked",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "leverage",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpCoreBase.Position",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "profitVaultAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        }
      ],
      "name": "pythOracleId",
      "outputs": [
        {
          "internalType": "bytes32",
          "name": "",
          "type": "bytes32"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "token",
          "type": "address"
        }
      ],
      "name": "queryPythPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        },
        {
          "internalType": "uint64",
          "name": "pubishTime",
          "type": "uint64"
        },
        {
          "internalType": "bool",
          "name": "isStale",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "isAllow",
          "type": "bool"
        }
      ],
      "name": "setAllowUnderlying",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "setBountyFeeRateToLiquidator",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "setBountyFeeRateToProtocol",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "newValue",
          "type": "uint256"
        }
      ],
      "name": "setDummyPrice",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "setFeeToProtocolRate",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "setLiquidatePnlRatio",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "setLiquidityRatio",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "maintenance",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "minimum",
          "type": "uint256"
        }
      ],
      "name": "setMarginRatio",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "int256",
          "name": "value",
          "type": "int256"
        }
      ],
      "name": "setMaxPnls",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "setMaximumOpenSize",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "value",
          "type": "uint256"
        }
      ],
      "name": "setMinimumOpenSize",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "tokenAddress",
          "type": "address"
        },
        {
          "internalType": "uint256[]",
          "name": "_fundingNetOI",
          "type": "uint256[]"
        },
        {
          "internalType": "uint256[]",
          "name": "_fundingRates",
          "type": "uint256[]"
        },
        {
          "internalType": "uint256[]",
          "name": "_spreadNotional",
          "type": "uint256[]"
        },
        {
          "internalType": "uint256[]",
          "name": "_spread",
          "type": "uint256[]"
        }
      ],
      "name": "setOIConfig",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_perpCloseTradingAddress",
          "type": "address"
        }
      ],
      "name": "setPerpCloseTrading",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_perpLendingAddress",
          "type": "address"
        }
      ],
      "name": "setPerpLending",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_perpTradingAddress",
          "type": "address"
        }
      ],
      "name": "setPerpTrading",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_perpWalletTradingAddress",
          "type": "address"
        }
      ],
      "name": "setPerpWalletTrading",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_profitVaultAddress",
          "type": "address"
        }
      ],
      "name": "setProfitVaultAddress",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "internalType": "bytes32",
          "name": "id",
          "type": "bytes32"
        }
      ],
      "name": "setPythId",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint64",
          "name": "period",
          "type": "uint64"
        }
      ],
      "name": "setStalePeriod",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "tpPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "slPrice",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "setTPSL",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlyingTokenAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "feeValue",
          "type": "uint256"
        }
      ],
      "name": "setTPSLExecutionFee",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "fee",
          "type": "uint256"
        }
      ],
      "name": "setTradingFee",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "stalePeriod",
      "outputs": [
        {
          "internalType": "uint64",
          "name": "",
          "type": "uint64"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "tokenAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        }
      ],
      "name": "tokenHolders",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "pToken",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "atpToken",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpCoreBase.PoolTokens",
          "name": "poolToken",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalFundingFee",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "totalTradingFee",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlyingAddress",
          "type": "address"
        }
      ],
      "name": "tpslExecutionFee",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        }
      ],
      "name": "tpsls",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "tpPrice",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "slPrice",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpCoreBase.TPSL",
          "name": "tpsl",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "underlying",
          "type": "address"
        }
      ],
      "name": "tradingFeeRates",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "token",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transferOut",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "triggerTPSL",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "updatePythPrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "leftoverFee",
          "type": "uint256"
        }
      ],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "withdrawAmount",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "withdraw",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "collateralToken",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "bytes[]",
          "name": "pythUpdateData",
          "type": "bytes[]"
        }
      ],
      "name": "withdrawCollateral",
      "outputs": [],
      "stateMutability": "payable",
      "type": "function"
    }
  ]

FWX_PERP_HELPER_ABI:list[dict[str,Any]] = [
    {
      "inputs": [],
      "name": "baseLogicAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "bytes32",
          "name": "id",
          "type": "bytes32"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "priceFeeds",
          "type": "tuple[]"
        }
      ],
      "name": "findPriceFeedsByID",
      "outputs": [
        {
          "components": [
            {
              "internalType": "int64",
              "name": "price",
              "type": "int64"
            },
            {
              "internalType": "uint64",
              "name": "conf",
              "type": "uint64"
            },
            {
              "internalType": "int32",
              "name": "expo",
              "type": "int32"
            },
            {
              "internalType": "uint256",
              "name": "publishTime",
              "type": "uint256"
            }
          ],
          "internalType": "struct PythStructs.Price",
          "name": "price",
          "type": "tuple"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingTokenAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "newAmount",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "isAdd",
          "type": "bool"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "priceFeeds",
          "type": "tuple[]"
        }
      ],
      "name": "getAdjustTradingCollateralInfo",
      "outputs": [
        {
          "components": [
            {
              "internalType": "int256",
              "name": "nextNetBalance",
              "type": "int256"
            },
            {
              "internalType": "uint256",
              "name": "nextAvailableBalance",
              "type": "uint256"
            },
            {
              "internalType": "int256",
              "name": "prevMargin",
              "type": "int256"
            },
            {
              "internalType": "int256",
              "name": "nextMargin",
              "type": "int256"
            },
            {
              "internalType": "uint256",
              "name": "prevLiqPrice",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "nextLiqPrice",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpHelper.AdjustTradingCollateralInfo",
          "name": "result",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "getAllActivePositions",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint64",
              "name": "id",
              "type": "uint64"
            },
            {
              "internalType": "bool",
              "name": "isLong",
              "type": "bool"
            },
            {
              "internalType": "address",
              "name": "collateral",
              "type": "address"
            },
            {
              "internalType": "address",
              "name": "underlying",
              "type": "address"
            },
            {
              "internalType": "uint128",
              "name": "entryPrice",
              "type": "uint128"
            },
            {
              "internalType": "uint128",
              "name": "currentPrice",
              "type": "uint128"
            },
            {
              "internalType": "uint128",
              "name": "contractSize",
              "type": "uint128"
            },
            {
              "internalType": "uint128",
              "name": "collateralSwappedAmount",
              "type": "uint128"
            },
            {
              "internalType": "uint256",
              "name": "liqPrice",
              "type": "uint256"
            },
            {
              "internalType": "int256",
              "name": "pnl",
              "type": "int256"
            },
            {
              "internalType": "int256",
              "name": "roe",
              "type": "int256"
            },
            {
              "internalType": "int256",
              "name": "margin",
              "type": "int256"
            },
            {
              "internalType": "uint256",
              "name": "leverage",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "tpPrice",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "slPrice",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpHelper.PositionData[]",
          "name": "data",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "getAllUnRealizedPNL",
      "outputs": [
        {
          "internalType": "int256",
          "name": "result",
          "type": "int256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "getBalance",
      "outputs": [
        {
          "internalType": "int256",
          "name": "netBalance",
          "type": "int256"
        },
        {
          "internalType": "uint256",
          "name": "availableBalance",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "collateralAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "underlyingAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "collateralAmount",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "leverage",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        }
      ],
      "name": "getContractSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "isNewLong",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "contractSize",
          "type": "uint256"
        }
      ],
      "name": "getCostFee",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "fundingFee",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "tradingFee",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "contractSize",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "isLong",
          "type": "bool"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed",
          "name": "pythPrice",
          "type": "tuple"
        }
      ],
      "name": "getEntryPriceAsPerturb",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "price",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "isAdd",
          "type": "bool"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "getLenderBalanceInfo",
      "outputs": [
        {
          "internalType": "bool",
          "name": "isError",
          "type": "bool"
        },
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "deposit",
              "type": "uint256"
            },
            {
              "internalType": "int256",
              "name": "pnl",
              "type": "int256"
            },
            {
              "internalType": "uint256",
              "name": "share",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "myBalance",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpHelper.LenderBalanceInfo",
          "name": "beforeBalance",
          "type": "tuple"
        },
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "deposit",
              "type": "uint256"
            },
            {
              "internalType": "int256",
              "name": "pnl",
              "type": "int256"
            },
            {
              "internalType": "uint256",
              "name": "share",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "myBalance",
              "type": "uint256"
            }
          ],
          "internalType": "struct IPerpHelper.LenderBalanceInfo",
          "name": "afterBalance",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "isNewLong",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "newContractSize",
          "type": "uint256"
        },
        {
          "internalType": "bool",
          "name": "isAdd",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "newAmount",
          "type": "uint256"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "getLiquidatePrice",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "liquidationPrice",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "isNewLong",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "leverage",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "safetyFactor",
          "type": "uint256"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "getMaxAndLimitContractSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "maxContractSize",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "limitContractSize",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "bool",
          "name": "isNewLong",
          "type": "bool"
        },
        {
          "internalType": "uint256",
          "name": "leverage",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "safetyFactor",
          "type": "uint256"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "getMaxContractSize",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "maxContractSize",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "address",
          "name": "underlyingToken",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "closingSize",
          "type": "uint256"
        },
        {
          "components": [
            {
              "internalType": "int64",
              "name": "price",
              "type": "int64"
            },
            {
              "internalType": "uint64",
              "name": "conf",
              "type": "uint64"
            },
            {
              "internalType": "int32",
              "name": "expo",
              "type": "int32"
            },
            {
              "internalType": "uint256",
              "name": "publishTime",
              "type": "uint256"
            }
          ],
          "internalType": "struct PythStructs.Price",
          "name": "price",
          "type": "tuple"
        }
      ],
      "name": "getPnlAndRoe",
      "outputs": [
        {
          "internalType": "int256",
          "name": "pnl",
          "type": "int256"
        },
        {
          "internalType": "int256",
          "name": "roe",
          "type": "int256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "getPoolBalanceInfo",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "TVL",
          "type": "uint256"
        },
        {
          "internalType": "int256",
          "name": "unrealizedPnl",
          "type": "int256"
        },
        {
          "internalType": "int256",
          "name": "availableLiquidity",
          "type": "int256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        }
      ],
      "name": "getPythIds",
      "outputs": [
        {
          "internalType": "bytes32[]",
          "name": "output",
          "type": "bytes32[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "contractSize",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "leverage",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "entryPrice",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "maxLeverage",
          "type": "uint256"
        }
      ],
      "name": "getRequiredCollateral",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "requiredCollateral",
          "type": "uint256"
        }
      ],
      "stateMutability": "pure",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "start",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "count",
          "type": "uint256"
        }
      ],
      "name": "getTotalCollateralLocked",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "totalCollateralLocked",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "coreAddress",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "nftId",
          "type": "uint256"
        },
        {
          "internalType": "uint256",
          "name": "posId",
          "type": "uint256"
        },
        {
          "components": [
            {
              "internalType": "bytes32",
              "name": "id",
              "type": "bytes32"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "price",
              "type": "tuple"
            },
            {
              "components": [
                {
                  "internalType": "int64",
                  "name": "price",
                  "type": "int64"
                },
                {
                  "internalType": "uint64",
                  "name": "conf",
                  "type": "uint64"
                },
                {
                  "internalType": "int32",
                  "name": "expo",
                  "type": "int32"
                },
                {
                  "internalType": "uint256",
                  "name": "publishTime",
                  "type": "uint256"
                }
              ],
              "internalType": "struct PythStructs.Price",
              "name": "emaPrice",
              "type": "tuple"
            }
          ],
          "internalType": "struct PythStructs.PriceFeed[]",
          "name": "prices",
          "type": "tuple[]"
        }
      ],
      "name": "isLiquidable",
      "outputs": [
        {
          "internalType": "bool",
          "name": "isPosLiquidable",
          "type": "bool"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "lendingAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "logicAddress",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "logicAddress2",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_logicAddress",
          "type": "address"
        }
      ],
      "name": "setPerpHelperBaseLogic",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_logicAddress",
          "type": "address"
        }
      ],
      "name": "setPerpHelperLending",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_logicAddress",
          "type": "address"
        }
      ],
      "name": "setPerpHelperLogic",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_logicAddress",
          "type": "address"
        }
      ],
      "name": "setPerpHelperLogic2",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]