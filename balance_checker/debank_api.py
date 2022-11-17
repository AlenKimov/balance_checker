import aiohttp
from aiohttp.client import ClientSession
import asyncio
import requests
from tqdm import tqdm
import random
from time import sleep

# Скрипты проекта
from logger import logger
from model import AddressData
from utils import cut_list


def update_data_list_address_balances_async(data_list: list[AddressData], limit: int = 8, timeout: int = 60):
    logger.info("Попытка запроса балансов адресов..")

    url = 'https://api.debank.com/user/addr'

    async def _get_usd_value(session: ClientSession, data: AddressData):
        response = await session.get(url, params={'addr': data.address})
        try:
            response_json = await response.json()
            data.balance = await response_json["data"].get('usd_value', 0)
            logger.success(f"[{data.address}] Баланс: ${data.balance:.1f}")
        except Exception:
            logger.error(f"[{data.address}] Не удалось запросить баланс")

    async def _get_address_balances(data_list: list[AddressData]):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for data in data_list:
                tasks.append(asyncio.create_task(_get_usd_value(session, data)))
            for task in tasks:
                await task
            await asyncio.gather(*tasks)

    data_list_parts = cut_list(data_list, limit)

    if len(data_list_parts) == 1:
        timeout = 0

    for data_list_part in tqdm(data_list_parts):
        asyncio.run(_get_address_balances(data_list_part))
        if timeout > 0:
            logger.info(f"Ожидание {timeout} секунд..")
            sleep(timeout)


def update_data_list_address_balances(data_list: list[AddressData], timeout: float = 5):
    url = 'https://api.debank.com/user/addr'
    session = requests.session()
    for data in tqdm(data_list):
        while data.balance is None:
            response = session.get(url, params={'addr': data.address})
            if response.status_code == 200:
                response_json = response.json()
                if response_json['error_code'] == 1:
                    logger.error(f"[{data.address}] Не удалось запросить баланс: неверный адрес")
                else:
                    data.balance = response_json["data"].get('usd_value', 0)
                    logger.success(f"[{data.address}] Баланс: ${data.balance:.1f}")
            else:
                logger.error(f"[{data.address}] Не удалось запросить баланс: ошибка {response.status_code}")
                logger.info(f"Ожидание {timeout:.2f} секунд..")
                sleep(timeout)


def get_social_ranking_addresses(page_to: int = 1) -> list[str]:
    url = "https://api.debank.com/social_ranking/list"

    addresses = list()
    for i in range(1, page_to + 1):
        querystring = {"page_num": i, "page_count": "50"}
        response = requests.request('GET', url, params=querystring)
        response_json = response.json()
        addresses.extend([data['id'] for data in response_json['data']['social_ranking_list']])

    return addresses
