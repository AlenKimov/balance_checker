from eth_account import Account
from eth_account.signers.local import LocalAccount

# Скрипты проекта
from config import addresses, private_keys, mnemonics
from logger import logger
from debank_api import get_address_balances
from output_funcs import save_to_output


def main():
    for private_key in private_keys:
        try:
            account: LocalAccount = Account.from_key(private_key=private_key)
            addresses.append(account.address)
        except Exception:
            logger.warning(f"[{private_key}] Неверный приватный ключ")

    for mnemonic in mnemonics:
        try:
            account: LocalAccount = Account.from_mnemonic(mnemonic=mnemonic)
            addresses.append(account.address)
        except Exception:
            logger.warning(f"[{mnemonic}] Неверная мнемоническая фраза")

    save_to_output(get_address_balances(addresses))


if __name__ == '__main__':
    main()
