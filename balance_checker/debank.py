import aiohttp
from aiohttp.client import ClientSession, ClientTimeout
import asyncio
import requests
from time import sleep
from pyuseragents import random as random_useragent

# Скрипты проекта
from logger import logger
from model import AddressData


client_timeout = ClientTimeout(total=100)


def update_data_list_balances(data_list: list[AddressData], limit: int = 5, timeout: int = 30):
    url = "https://api.debank.com/user/total_balance"

    async def _get_usd_value(session: ClientSession, data: AddressData):
        response = await session.get(url, params={'addr': data.address})
        try:
            response_json = await response.json()
            data.balance = response_json["data"].get('total_usd_value', 0)
            logger.success(f"[{data.address}] Balance: ${data.balance:.1f}")
        except Exception:
            logger.error(f"[{data.address}] Failed to request a balance")

    async def _get_address_balances(data_list: list[AddressData]):
        headers = {'user-agent': random_useragent()}
        async with aiohttp.ClientSession(headers=headers, timeout=client_timeout) as session:
            tasks = []
            for data in data_list:
                tasks.append(asyncio.create_task(_get_usd_value(session, data)))
            for task in tasks:
                await task
            await asyncio.gather(*tasks)

    undone_data = data_list.copy()
    logger.info(f"Total addresses: {len(undone_data)}")
    while undone_data:
        asyncio.run(_get_address_balances(undone_data[:limit]))
        undone_data = [data for data in undone_data if data.balance is None]
        logger.info(f"Addresses left: {len(undone_data)}")
        if timeout > 0 and undone_data:
            logger.info(f"Waiting {timeout} seconds..")
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
