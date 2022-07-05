"""
Example entrypoint for Task №2.
"""
import asyncio
from collections import defaultdict

from task2.solution import iter_russian_wiki_animal_names


async def main():
    counter = defaultdict(int)
    async for animal_name in iter_russian_wiki_animal_names():
        first_letter = animal_name[0].upper()
        counter[first_letter] += 1

    for letter, amount in counter.items():
        print(f'{letter}: {amount}')


if __name__ == '__main__':
    asyncio.run(main())
