import urllib
from http import HTTPStatus
from typing import AsyncIterator
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

from utils.algorithms import find_first


async def iter_by_ru_wiki_animal_names() -> AsyncIterator[str]:
    """
    Iterate over animal names on Wiki (Russian and English).
    """
    params = {
        'title': 'Категория:Животные_по_алфавиту',
    }
    base_url = 'https://ru.wikipedia.org/w/index.php'
    next_page_link = base_url + '?' + urllib.parse.urlencode(params)
    async with httpx.AsyncClient() as client:
        while True:
            response = await client.get(next_page_link)
            soup = BeautifulSoup(response.text, 'html.parser')
            assert response.status_code == HTTPStatus.OK, \
                f'Response error status code: {response.status_code}'

            # parse animal names
            animal_names_el = soup.select(
                '.mw-category.mw-category-columns li')
            if not animal_names_el:
                break

            for animal_name in animal_names_el:
                yield animal_name.text

            # parse next page link
            links_el = soup.select('a[href$="#mw-pages"]')
            assert links_el, 'Links were not found'
            next_page_link_el = find_first(
                lambda link_el: link_el.text.strip() == 'Следующая страница',
                links_el
            )
            if not next_page_link_el:
                break

            next_page_href = next_page_link_el.get('href', None)
            assert next_page_href, f'Invalid link string: {next_page_href}'
            next_page_link = urljoin(
                base=base_url, url=next_page_href)  # type: ignore


async def iter_russian_wiki_animal_names():
    """
    Iterate over Russian Wiki animal names.
    """
    async for animal_name in iter_by_ru_wiki_animal_names():
        if animal_name.lower().startswith('a'):
            break
        yield animal_name
