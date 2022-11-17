from os import makedirs
from datetime import datetime
from pathlib import Path
import json
import toml

# Скрипты проекта
from logger import logger
from definitions import OUTPUT_DIR
from model import AddressData


makedirs(OUTPUT_DIR, exist_ok=True)


def save_data_list_to_output(data_list: list[AddressData]):
    logger.info(f'Попытка записи данных об адресах..')
    json_data_to_dump = [data.dict() for data in data_list if data.balance is not None and data.balance > 0]
    toml_data_to_dump = {data.address: data.dict() for data in data_list if data.balance is not None and data.balance > 0}
    if json_data_to_dump and toml_data_to_dump:
        now_datetime = f'{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}'
        new_output_dir = Path(OUTPUT_DIR, now_datetime)
        makedirs(new_output_dir)

        output_json_name = f'{now_datetime}.json'
        output_json_path = Path(new_output_dir, output_json_name)
        with open(output_json_path, 'w', encoding='utf-8') as output_json:
            if json_data_to_dump: json.dump(json_data_to_dump, output_json, indent=4)

        output_toml_name = f'{now_datetime}.toml'
        output_toml_path = Path(new_output_dir, output_toml_name)
        with open(output_toml_path, 'w', encoding='utf-8') as output_toml:
            if toml_data_to_dump: toml.dump(toml_data_to_dump, output_toml)

        logger.success(f'[{new_output_dir}] Данные об адресах успешно записаны')
    else:
        logger.warning(f'Адресов с балансами не обнаружено')
