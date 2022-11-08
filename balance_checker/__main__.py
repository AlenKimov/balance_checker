from eth_account import Account
from eth_account.signers.local import LocalAccount

# Скрипты проекта
from config import addresses, private_keys, mnemonics
from debank_api import get_address_balances
from output_funcs import save_to_output


def main():
    for private_key in private_keys:
        account: LocalAccount = Account.from_key(private_key=private_key)
        addresses.append(account.address)

    for mnemonic in mnemonics:
        account: LocalAccount = Account.from_mnemonic(mnemonic=mnemonic)
        addresses.append(account.address)

    save_to_output(get_address_balances(addresses))


if __name__ == '__main__':
    main()
