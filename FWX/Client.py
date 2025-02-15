from hexbytes import HexBytes
from web3 import Web3
import requests
from typing import (
    Any,
)
from eth_typing import (
    ChecksumAddress,
)
from web3.types import (
    Wei
)

from .Constant import(
    USDC_BASE,
    USDC_AVALANCHE
)

from .types import (
    TxParamsInput,
    FWXPerpHelperGetAllPositionRespond,
    FWXPerpHelperGetBalanceRespond
)
from .W3 import (
    Web3WalletHTTP,
)
from .Contract import (
    ERC20Contract,
    FWXMembershipContract,
    FWXPerpCoreContract,
    FWXPerpHelperContract,
)

def get_fwx_raw_pyth_data() -> dict[str,Any]:
    url = 'https://hermes-pyth.fwx.finance/?pyth=perp&encoding=hex'
    data = requests.get(url).json()
    return data

def create_pyth_data(raw_pyth_data:dict[str,Any])->list[tuple[bytes,tuple[int,...],tuple[int,...]]]:
    pyth_data:list[tuple[bytes,tuple[int,...],tuple[int,...]]] = []
    for i in raw_pyth_data['parsed']:
        
        id:bytes = bytes.fromhex(i['id'])
        price:tuple[int,...] = tuple([int(j) for j in i['price'].values()])
        ema_price:tuple[int,...] = tuple([int(j) for j in i['ema_price'].values()])
        d:tuple[bytes,tuple[int,...],tuple[int,...]] = (id,price,ema_price)
        pyth_data.append(d)
        
    return pyth_data

def create_pyth_update_data(raw_pyth_data:dict[str,Any])->list[bytes]:
    
    return [bytes.fromhex(raw_pyth_data['binary']['data'][0])]

class FWXClient(Web3WalletHTTP):
    """
    FWXClient is a client for interacting with the FWX Membership Contract.
    
    Attributes:
        membership (FWXMembershipContract): Instance of the FWXMembershipContract.
        nft_id (int): The ID of the NFT representing the membership.
    """
    
    def __init__(self, 
                 provider: str, 
                 private_key: str,
                 refferal_id: int = 0) -> None:
        """
        Initializes the FWXClient with the given provider, private key, and optional referral ID.
        
        Args:
            provider (str): The provider URL for the blockchain connection.
            private_key (str): The private key for the wallet.
            refferal_id (int, optional): The referral ID for minting membership. Defaults to 0.
        """
        super().__init__(provider, private_key)
        self.membership = FWXMembershipContract(provider)
        self.nft_id = self.membership.get_default_membership(self.wallet_address)
        if self.nft_id == 0:
            print('This address is not a member')
            print('Minting membership')
            mint_func = self.membership.mint(refferal_id)
            self.build_and_send_transaction(func=mint_func)
            print('Membership minted')
            self.nft_id = self.membership.get_default_membership(self.wallet_address)
            
        print(f'Membership ID: {self.nft_id}')

class FWXPerpClient(FWXClient):
    
    def __init__(self, provider: str, private_key: str, refferal_id: int = 0) -> None:
        """
        Initialize the Client object.
        Args:
            provider (str): The provider URL or identifier.
            private_key (str): The private key for authentication.
            refferal_id (int, optional): The referral ID. Defaults to 0.
        Raises:
            Exception: If the chain ID is not supported.
        Example:
            client = Client(provider="https://mainnet.infura.io/v3/YOUR-PROJECT-ID", 
                            private_key="your_private_key", 
                            refferal_id=12345)
        """
        super().__init__(provider, private_key,refferal_id)
        self.core = FWXPerpCoreContract(provider)
        self.helper = FWXPerpHelperContract(provider)
        
        match self.chain_id:
            case 8453:
                self.usdc = ERC20Contract(provider,USDC_BASE)
            case 43114:
                self.usdc = ERC20Contract(provider,USDC_AVALANCHE)
            case _:
                raise Exception('Chain ID not supported')
                
    def get_perp_balance(self) -> FWXPerpHelperGetBalanceRespond:
        """
        Retrieve the perpetual balance for the current user.
        This method fetches raw FWX Pyth data, processes it into a usable format,
        and then retrieves the balance using the helper's get_balance method.
        Returns:
            FWXPerpHelperGetBalanceRespond: The balance response object.
        Example:
            balance = client.get_perp_balance()
            print("net balance:", balance.net_balance)
            print("avaliable balance:", balance.avaliable_balance)
        Output:
            net balance: 1000000000000000000
            avaliable balance: 1000000000000000000
        """
        raw_fwx_pyth_data = get_fwx_raw_pyth_data()
        pyth_data = create_pyth_data(raw_fwx_pyth_data)
        
        return self.helper.get_balance(self.core.address,self.nft_id,pyth_data)
    
    def get_all_positions(self) -> list[FWXPerpHelperGetAllPositionRespond]|None:
        """
        Retrieve all active positions for the current user.
        This method fetches raw FWX Pyth data, processes it into a usable format,
        and then retrieves all active positions using the helper's get_all_active_positions method.
        Returns:
            list[FWXPerpHelperGetAllPositionRespond] | None: A list of position response objects or None if no positions are found.
        Example:
            positions = client.get_all_positions()
            if positions:
                for position in positions:
                    print("Position ID:", position.id)
                    print("Position Size:", position.size)
            else:
                print("No active positions found.")
        Output:
            Position ID: 12345
            Position Size: 10
        """
        raw_fwx_pyth_data = get_fwx_raw_pyth_data()
        pyth_data = create_pyth_data(raw_fwx_pyth_data)
        
        return self.helper.get_all_active_positions(self.core.address,self.nft_id,pyth_data)
    
    def deposite_collateral(self,
                            amount:Wei,
                            underlying_address:ChecksumAddress,
                            tx_params_input:TxParamsInput=TxParamsInput(),)->HexBytes:
        """
        Deposit collateral into the system.
        This method approves the necessary amount of USDC, constructs the deposit transaction,
        sends it, and waits for the transaction receipt.
        Args:
            amount (Wei): The amount of collateral to deposit.
            underlying_address (ChecksumAddress): The address of the underlying asset.
            tx_params_input (TxParamsInput, optional): Transaction parameters. Defaults to TxParamsInput().
        Returns:
            HexBytes: The transaction hash.
        Example:
            txn = client.deposite_collateral(amount=1000, underlying_address="0x1234567890abcdef1234567890abcdef12345678")
            print("Transaction hash:", txn.hex())
        Output:
            Transaction hash: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
        """
        
        self.usdc.check_approval(self,self.core.address,amount)
        deposite_func = self.core.depositCollateral(self.nft_id,self.usdc.address,underlying_address,amount)
        txn = self.build_and_send_transaction(func=deposite_func,tx_params_input=tx_params_input)
        self.w3.eth.wait_for_transaction_receipt(txn)
        
        return txn
    
    def _openPositionGivenContractSize(self,
                                      is_long: bool,
                                      contract_size: int,
                                      leverage: int,
                                      underlying_address: ChecksumAddress,
                                      raw_pyth_data: dict[str, Any],
                                      tx_params_input: TxParamsInput = TxParamsInput()) -> HexBytes:
        """
        Open a position given the contract size.
        This method constructs the necessary transaction to open a position with the specified parameters,
        sends it, and waits for the transaction receipt.
        
        Args:
            is_long (bool): Indicates if the position is long.
            contract_size (int): The size of the contract.
            leverage (int): The leverage to be applied.
            underlying_address (ChecksumAddress): The address of the underlying asset.
            raw_pyth_data (dict[str, Any]): The raw data from Pyth.
            tx_params_input (TxParamsInput, optional): Transaction parameters. Defaults to TxParamsInput().
        
        Returns:
            HexBytes: The transaction hash.
        
        Example:
            txn = client._openPositionGivenContractSize(
                is_long=True,
                contract_size=10,
                leverage=5,
                underlying_address="0x1234567890abcdef1234567890abcdef12345678",
                raw_pyth_data={"parsed": [], "binary": []}
            )
            print("Transaction hash:", txn.hex())
        
        Output:
            Transaction hash: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
        """
        leverage = leverage*10**18
        pyth_updata_data = create_pyth_update_data(raw_pyth_data)
        value = len(raw_pyth_data['parsed']) + len(raw_pyth_data['binary'])
        func = self.core.openPosition(self.nft_id,
                                      is_long,
                                      self.usdc.address,
                                      underlying_address,
                                      contract_size,
                                      leverage,
                                      pyth_updata_data,)
        tx_params_input = tx_params_input._replace(value=value)
        txn = self.build_and_send_transaction(func=func,tx_params_input=tx_params_input)
        self.w3.eth.wait_for_transaction_receipt(txn)
        return txn
    
    def get_max_contract_size(self,
                              underlying_address:ChecksumAddress,
                              raw_pyth_data:dict[str,Any],
                              is_new_long:bool,
                              leverage:int=1,
                              safety_factor:int=980000)->int:
        """
        Calculate the maximum contract size for a given underlying asset.
        Args:
            underlying_address (ChecksumAddress): The address of the underlying asset.
            raw_pyth_data (dict[str, Any]): Raw data from the Pyth network.
            is_new_long (bool): Indicates if the position is a new long position.
            leverage (int, optional): The leverage to be applied. Defaults to 1.
            safety_factor (int, optional): The safety factor to be applied. Defaults to 980000.
        Returns:
            int: The maximum contract size.
        Example:
            max_contract_size = client.get_max_contract_size(
                underlying_address="0x1234567890abcdef1234567890abcdef12345678",
                raw_pyth_data=pyth_data,
                is_new_long=True,
                leverage=2,
                safety_factor=950000
            )
            print("Max Contract Size:", max_contract_size)
            
        Output:
            Max Contract Size: 1000000000000000000
        """
        pyth_data = create_pyth_data(raw_pyth_data)
        leverage = leverage*10**18
        
        return self.helper.get_max_contract_size(self.core.address,
                                                self.nft_id,
                                                underlying_address,
                                                is_new_long,
                                                leverage,
                                                safety_factor,
                                                pyth_data)
        
    def get_contract_size_given_volumn(self,
                                       volume: float,
                                       raw_pyth_data: dict[str, Any],
                                       pyth_id: str) -> float:
        """
        Calculate the contract size given a volume and Pyth data.
        This method calculates the contract size based on the provided volume and 
        the Pyth data. It searches for the specified Pyth ID in the raw Pyth data 
        and uses the associated price to compute the contract size.
        Args:
            volume (float): The volume for which the contract size is to be calculated.
            raw_pyth_data (dict[str, Any]): The raw Pyth data containing price information.
            pyth_id (str): The Pyth ID to search for in the raw Pyth data.
        Returns:
            float: The calculated contract size.
        Raises:
            Exception: If the specified Pyth ID is not found in the raw Pyth data.
        Example:
            raw_pyth_data = {
                'parsed': [
                    {
                        'id': 'example_id',
                        'price': {
                            'price': 100,
                            'expo': -2
                        }
                    }
                ]
            }
            volume = 1000.0
            pyth_id = 'example_id'
            contract_size = get_contract_size_given_volumn(volume, raw_pyth_data, pyth_id)
            print(contract_size)  
        Output:
            10.0
        """
        contract_size = 0
        for i in raw_pyth_data['parsed']:
            if i['id'] == pyth_id:
                price = int(i['price']['price'])*10**i['price']['expo']
                contract_size = volume/price
                break
        if contract_size == 0:
            raise Exception('Pyth ID not found')
        
        return contract_size
    
    def open_position_given_contract_size(self,
                                          is_long:bool,
                                          contract_size:int,
                                          leverage:int,
                                          underlying_address:ChecksumAddress,
                                          raw_pyth_data:dict[str,Any],
                                          is_new_long:bool,
                                          open_at_max:bool=True,
                                          tx_params_input:TxParamsInput=TxParamsInput())->HexBytes:
        """
        Open a position given the contract size.
        Args:
            is_long (bool): Indicates if the position is long.
            contract_size (int): The size of the contract to open.
            leverage (int): The leverage to be applied.
            underlying_address (ChecksumAddress): The address of the underlying asset.
            raw_pyth_data (dict[str, Any]): Raw data from the Pyth network.
            is_new_long (bool): Indicates if the position is a new long position.
            open_at_max (bool, optional): If True, open the position at the maximum contract size. Defaults to True.
            tx_params_input (TxParamsInput, optional): Transaction parameters input. Defaults to TxParamsInput().
        Returns:
            HexBytes: The transaction hash of the opened position.
        Raises:
            ValueError: If the contract size is too large.
        Example:
            tx_hash = client.open_position_given_contract_size(
                is_long=True,
                contract_size=10,
                leverage=2,
                underlying_address="0x1234567890abcdef1234567890abcdef12345678",
                raw_pyth_data=pyth_data,
                is_new_long=True,
                open_at_max=False
            )
            print("Transaction Hash:", tx_hash.hex())
        Output:
            Transaction Hash: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
        """
        max_contract_size = self.get_max_contract_size(underlying_address,
                                                       raw_pyth_data,
                                                       is_new_long,leverage)
        
        contract_size = Web3.to_wei(contract_size,'ether')
        if open_at_max:
            contract_size = min(contract_size,max_contract_size)
            
        else:
            if contract_size > max_contract_size:
                raise ValueError("Contract size is too large")
            
        return self._openPositionGivenContractSize(is_long,
                                                   contract_size,
                                                   leverage,
                                                   underlying_address,
                                                   raw_pyth_data,
                                                   tx_params_input)
        
    def open_position_given_volume(self,
                                   is_long:bool,
                                   volume:float,
                                   leverage:int,
                                   underlying_address:ChecksumAddress,
                                   raw_pyth_data:dict[str,Any],
                                   is_new_long:bool,
                                   pyth_id:str,
                                   open_at_max:bool=True,
                                   tx_params_input:TxParamsInput=TxParamsInput())->HexBytes:
        """
        Open a position given the volume.
        Args:
            is_long (bool): Indicates if the position is long.
            volume (float): The volume of the position to open.
            leverage (int): The leverage to be applied.
            underlying_address (ChecksumAddress): The address of the underlying asset.
            raw_pyth_data (dict[str, Any]): Raw data from the Pyth network.
            is_new_long (bool): Indicates if the position is a new long position.
            pyth_id (str): The Pyth network identifier.
            open_at_max (bool, optional): If True, open the position at the maximum contract size. Defaults to True.
            tx_params_input (TxParamsInput, optional): Transaction parameters input. Defaults to TxParamsInput().
        Returns:
            HexBytes: The transaction hash of the opened position.
        Raises:
            ValueError: If the volume is invalid.
        Example:
            tx_hash = client.open_position_given_volume(
                is_long=True,
                volume=1000.0,
                leverage=2,
                underlying_address="0x1234567890abcdef1234567890abcdef12345678",
                raw_pyth_data=pyth_data,
                is_new_long=True,
                pyth_id="pyth123",
                open_at_max=False
            )
            print("Transaction Hash:", tx_hash.hex())
        Output:
            Transaction Hash: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
        """
        
        contract_size = Wei(int(self.get_contract_size_given_volumn(volume,raw_pyth_data,pyth_id)))
        
        return self.open_position_given_contract_size(is_long,
                                                      contract_size,
                                                      leverage,
                                                      underlying_address,
                                                      raw_pyth_data,
                                                      is_new_long,
                                                      open_at_max,
                                                      tx_params_input)
        
    def close_position(self,
                       pos_id:int,
                       closing_size:float,
                       raw_pyth_data:dict[str,Any],
                       tx_params_input:TxParamsInput=TxParamsInput(),)->HexBytes:
        """
        Close a position.
        Args:
            pos_id (int): The ID of the position to close.
            closing_size (float): The size of the position to close.
            raw_pyth_data (dict[str, Any]): Raw data from the Pyth network.
            tx_params_input (TxParamsInput, optional): Transaction parameters input. Defaults to TxParamsInput().
        Returns:

            HexBytes: The transaction hash of the closed position.
        Raises:

            ValueError: If the closing size is invalid.
        Example:
            
                tx_hash = client.close_position(
                    pos_id=12345,
                    closing_size=10.0,
                    raw_pyth_data=pyth_data
                )
                print("Transaction Hash:", tx_hash.hex())
                
        Output:
            Transaction Hash: 0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890
        """
        
        value = len(raw_pyth_data['parsed']) + len(raw_pyth_data['binary'])
        pyth_update_data = create_pyth_update_data(raw_pyth_data)
        closing_size = Web3.to_wei(closing_size,'ether')
        func =  self.core.closePosition(self.nft_id,
                                        pos_id,
                                        closing_size,
                                        pyth_update_data=pyth_update_data)
        tx_params_input = tx_params_input._replace(value=value)
        txn = self.build_and_send_transaction(func=func,tx_params_input=tx_params_input)
        self.w3.eth.wait_for_transaction_receipt(txn)
        return txn