from eth_account import Account
from eth_account.signers.local import LocalAccount
import eth_utils

# Скрипты проекта
from logger import logger
from model import AddressData


def create_data_list(addresses: list[str] = None,
                     private_keys: list[str] = None,
                     mnemonics: list[str] = None
                     ) -> list[AddressData]:
    data_list: list[AddressData] = list()

    if addresses:
        for address in addresses:
            data_list.append(AddressData(address=address))

    if private_keys:
        for private_key in private_keys:
            try:
                account: LocalAccount = Account.from_key(private_key=private_key)
                data_list.append(AddressData(address=account.address, private_key=private_key))
            except Exception:  # binascii.Error
                logger.error(f"[{private_key}] Wrong private key")

    if mnemonics:
        Account.enable_unaudited_hdwallet_features()
        for mnemonic in mnemonics:
            try:
                account: LocalAccount = Account.from_mnemonic(mnemonic=mnemonic)
                data_list.append(AddressData(address=account.address, mnemonic=mnemonic))
            except eth_utils.exceptions.ValidationError:
                logger.error(f"[{mnemonic}] Wrong mnemonic")

    return data_list
