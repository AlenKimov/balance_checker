from eth_account import Account
from eth_account.signers.local import LocalAccount
import eth_utils

# Скрипты проекта
from config import addresses, private_keys, mnemonics, settings
from logger import logger
from model import AddressData
from debank_api import update_data_list_address_balances
from output import save_data_list_to_output


def main():
    data_list: list[AddressData] = list()

    for address in addresses:
        data_list.append(AddressData(address=address))

    for private_key in private_keys:
        try:
            account: LocalAccount = Account.from_key(private_key=private_key)
            data_list.append(AddressData(address=account.address, private_key=private_key))
        except Exception:  # binascii.Error
            logger.error(f"[{private_key}] Неверный приватный ключ")

    Account.enable_unaudited_hdwallet_features()
    for mnemonic in mnemonics:
        try:
            account: LocalAccount = Account.from_mnemonic(mnemonic=mnemonic)
            data_list.append(AddressData(address=account.address, mnemonic=mnemonic))
        except eth_utils.exceptions.ValidationError:
            logger.error(f"[{mnemonic}] Неверная мнемоническая фраза")

    update_data_list_address_balances(data_list)
    save_data_list_to_output(data_list)


if __name__ == '__main__':
    main()
