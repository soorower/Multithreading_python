import aiohttp
import asyncio
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
df = pd.read_excel('dnb.xlsx')
links = df['DnB Link'].to_list()[:50]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Safari/537.36'
}


def fetch(session, url):
    with session.get(url, headers=headers) as response:
        r = response.content
        soup = BeautifulSoup(r, 'lxml')
        for link in soup.findAll('a', attrs={'class': '_3gf3d xQBnN _1oHwA'}):
            links = link.get('href')
            links1 = f'https://exchangemarketplace.com{links}'
        print(links1)


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        with requests.Session() as session:
            for i in range(1, 20):
                executor.map(fetch, [session], [
                             f'https://exchangemarketplace.com/shops?page={i}&sortBy=createdAtHighToLow'])
            executor.shutdown(wait=True)


main()
# func()
