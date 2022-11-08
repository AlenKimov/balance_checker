from os import makedirs
from datetime import datetime
from pathlib import Path

# Скрипты проекта
from definitions import OUTPUT_DIR
from model import AddressData


def save_to_output(data_list: list[AddressData]):
    makedirs(OUTPUT_DIR, exist_ok=True)
    output_txt_name = f'{datetime.now().strftime("%d-%m-%Y %H:%M:%S")}.txt'
    output_txt_path = Path(OUTPUT_DIR, output_txt_name)
    with open(output_txt_path, 'w+', encoding='utf-8') as output_txt:
        for address_data in data_list:
            if address_data.balance > 0:
                output_txt.write(f'{address_data.address} ${address_data.balance}')
