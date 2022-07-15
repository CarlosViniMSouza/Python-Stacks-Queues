import argparse
import asyncio
import aiohttp
from collections import Counter

async def main(args):
    session = aiohttp.ClientSession()

    try:
        links = Counter()
        display(links)
    finally:
        await session.close()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("URL")
    parser.add_argument("-d", "--max-depth", type=int, default=2)
    parser.add_argument("-w", "--num-workers", type=int, default=3)

    return parser.parse_args()

def display(links):
    for URL, count in links.most_common():
        print(f"{count :> 3} {URL}")


if __name__ == "__main__":
    asyncio.run(main(parse_args()))