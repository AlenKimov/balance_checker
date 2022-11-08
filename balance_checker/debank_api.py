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


def get_address_balances(addresses: list[str], limit: int = 8, timeout: int = 21) -> list[AddressData]:
    logger.info("Пытаюсь запросить балансы адресов..")
    data_list: list[AddressData] = list()

    url = 'https://api.debank.com/user/addr'

    async def _get_usd_value(session: ClientSession, address: str):
        response = await session.get(url, params={'addr': address})
        try:
            response_json = await response.json()
            usd_value = response_json["data"].get('usd_value', 0)
            data_list.append(AddressData(address=address, balance=usd_value))
            logger.success(f"[{address}] Баланс: ${usd_value:.1f}")
        except Exception:
            logger.error(f"[{address}] Не удалось запросить баланс")

    async def _get_address_balances(addresses: list[str]):
        headers = {'user-agent': random_useragent()}
        async with aiohttp.ClientSession(headers=headers) as session:
            tasks = []
            for address in addresses:
                tasks.append(asyncio.create_task(_get_usd_value(session, address)))
            for task in tasks:
                await task
            await asyncio.gather(*tasks)

    addresses_parts = cut_list(addresses, limit)
    if len(addresses_parts) < 2:
        timeout = 0

    for addresses_part in tqdm(addresses_parts):
        asyncio.run(_get_address_balances(addresses_part))
        if timeout > 0:
            logger.info(f"Жду {timeout} секунд..")
            sleep(timeout)
    return data_list
