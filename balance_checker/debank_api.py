import aiohttp
import asyncio
from tqdm import tqdm
from aiohttp.client import ClientSession
from pyuseragents import random as random_useragent
from time import sleep

# Скрипты проекта
from logger import logger
from model import AddressData
from utils import cut_list


def update_data_list_address_balances(data_list: list[AddressData], limit: int = 8, timeout: int = 60):
    logger.info("Пытаюсь запросить балансы адресов..")

    url = 'https://api.debank.com/user/addr'

    async def _get_usd_value(session: ClientSession, data: AddressData):
        response = await session.get(url, params={'addr': data.address})
        try:
            response_json = await response.json()
            data.balance = response_json["data"].get('usd_value', 0)
            logger.success(f"[{data.address}] Баланс: ${data.balance:.1f}")
        except Exception:
            logger.error(f"[{data.address}] Не удалось запросить баланс")

    async def _get_address_balances(data_list: list[AddressData]):
        headers = {'user-agent': random_useragent()}
        async with aiohttp.ClientSession(headers=headers) as session:
            tasks = []
            for data in data_list:
                tasks.append(asyncio.create_task(_get_usd_value(session, data)))
            for task in tasks:
                await task
            await asyncio.gather(*tasks)

    data_list_parts = cut_list(data_list, limit)
    if len(data_list_parts) < 2:
        timeout = 0

    for data_list_part in tqdm(data_list_parts):
        asyncio.run(_get_address_balances(data_list_part))
        if timeout > 0:
            logger.info(f"Жду {timeout} секунд..")
            sleep(timeout)
