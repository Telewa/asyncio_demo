import asyncio
import sys
from os.path import basename

from aiohttp import ClientSession

from utils import safe_file_name, download_and_save


async def main():
    # download these three files in parallel
    async with ClientSession() as session:
        tasks = [
            download_and_save(filename=safe_file_name(basename(link)), url=link, session=session) for link in [
                "https://www.pgnmentor.com/players/Carlsen.zip",
                "https://www.pgnmentor.com/players/Kramnik.zip",
                "https://www.pgnmentor.com/players/So.zip",
                "https://www.pgnmentor.com/openings/GrunfeldFianchetto.zip",
                "https://www.pgnmentor.com/openings/KIDClassical.zip",
                "https://www.pgnmentor.com/openings/NimzoSaemisch.zip",
                "https://www.pgnmentor.com/openings/DutchClassical.zip"
            ]
        ]

        await asyncio.gather(*tasks)


if __name__ == "__main__":
    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."

    import time

    start_time = time.perf_counter()

    asyncio.run(main())

    end_time = time.perf_counter()
    elapsed = end_time - start_time

    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
