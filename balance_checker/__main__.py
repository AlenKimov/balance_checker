# Скрипты проекта
from config import settings, addresses, private_keys, mnemonics
from data_list import create_data_list
from debank import update_data_list_balances
from output import save_data_list_to_output


def main():
    data_list = create_data_list(addresses, private_keys, mnemonics)
    try:
        update_data_list_balances(data_list, timeout=settings.TIMEOUT, limit=settings.LIMIT)
    finally:
        save_data_list_to_output(data_list)


if __name__ == '__main__':
    main()
