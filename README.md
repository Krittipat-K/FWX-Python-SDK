# FWX-Python-SDK

This is an unofficial Python SDK for interacting with the FWX blockchain. It provides a set of tools and utilities to facilitate the development of applications on the FWX network.

## Disclaimer

This SDK is not officially supported or endorsed by the FWX team. Use it at your own risk. The authors of this SDK are not responsible for any issues or damages that may arise from using this software.

## Installation

To install the SDK, you can use pip:

```sh
pip install git+https://github.com/Krittipat-K/FWX-Python-SDK
```

## Usage

### Initializing the FWXClient

To start using the SDK, you need to initialize the `FWXClient` with your provider URL and private key.

```python
from FWX.Client import FWXClient

provider = "https://mainnet.infura.io/v3/YOUR-PROJECT-ID"
private_key = "your_private_key"
client = FWXClient(provider, private_key)
```

### Checking Membership

The `FWXClient` will automatically check if the wallet address is a member of the FWX Membership Contract. If not, it will mint a new membership.

```python
print(f'Membership ID: {client.nft_id}')
```

### Using FWXPerpClient

The `FWXPerpClient` extends `FWXClient` and provides additional functionalities for interacting with the FWX Perpetual Contracts.

```python
from FWX.Client import FWXPerpClient

perp_client = FWXPerpClient(provider, private_key)
```

### Retrieving Perpetual Balance

You can retrieve the perpetual balance for the current user using the `get_perp_balance` method.

```python
balance = perp_client.get_perp_balance()
print("Net Balance:", balance.net_balance)
print("Available Balance:", balance.available_balance)
```

### Retrieving All Positions

To retrieve all active positions for the current user, use the `get_all_positions` method.

```python
positions = perp_client.get_all_positions()
if positions:
    for position in positions:
        print("Position ID:", position.id)
        print("Position Size:", position.size)
else:
    print("No active positions found.")
```

### Depositing Collateral

To deposit collateral into the system, use the `deposit_collateral` method.

```python
from web3 import Web3
from eth_typing import ChecksumAddress

amount = Web3.toWei(1000, 'ether')
underlying_address = "0x1234567890abcdef1234567890abcdef12345678"
txn = perp_client.deposit_collateral(amount, underlying_address)
print("Transaction hash:", txn.hex())
```

### Opening a Position

To open a position given the contract size, use the `open_position_given_contract_size` method.

```python
raw_pyth_data = {
    'parsed': [
        {
            'id': 'example_id',
            'price': {
                'price': 100,
                'expo': -2
            }
        }
    ],
    'binary': []
}
is_long = True
contract_size = 10
leverage = 5
underlying_address = "0x1234567890abcdef1234567890abcdef12345678"
txn = perp_client.open_position_given_contract_size(is_long, contract_size, leverage, underlying_address, raw_pyth_data, is_new_long=True)
print("Transaction hash:", txn.hex())
```

### Closing a Position

To close a position, use the `close_position` method.

```python
pos_id = 12345
closing_size = 10.0
txn = perp_client.close_position(pos_id, closing_size, raw_pyth_data)
print("Transaction hash:", txn.hex())
```

This tutorial covers the basic usage of the FWX-Python-SDK. For more advanced functionalities, refer to the source code and the provided docstrings.


