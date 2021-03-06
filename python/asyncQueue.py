import sys
import argparse
import asyncio
import aiohttp
from typing import NamedTuple
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urljoin


class Job(NamedTuple):
    url: str
    depth: int = 1

    def __lt__(self, other):
        if isinstance(other, Job):
            return len(self.url) < len(other.url)


async def main(args):
    session = aiohttp.ClientSession()

    try:
        links = Counter()
        queue = asyncio.PriorityQueue()
        tasks = [
            asyncio.create_task(
                worker(
                    f"Worker - {i + 1}",
                    session,
                    queue,
                    links,
                    args.max_depth,
                )
            )
            for i in range(args.num_workers)
        ]

        await queue.put(Job(args.URL))
        await queue.join()

        for task in tasks:
            task.cancel()

        await asyncio.gather(*tasks, return_exceptions=True)

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

async def fetchHTML(session, url):
    async with session.get(url) as response:
        if response.ok and response.content_type == "text/html":
            return await response.text()

def parse_links(url, html):
    soup = BeautifulSoup(html, features="html.parser")
    for anchor in soup.select("a[href]"):
        href = anchor.get("href").lower()

        if not href.startswith("javascript:"):
            yield urljoin(url, href)

async def worker(workerID, session, queue, links, maxDepth):
    print(f"[{workerID} starting]", file=sys.stderr)

    while True:
        url, depth = await queue.get()
        links[url] += 1
        try:
            if depth <= maxDepth:
                print(f"[{workerID} {depth =} {url =}]",
                      file=sys.stderr)

                if html := await fetchHTML(session, html):
                    for linkURL in parse_links(url, html):
                        await queue.put(Job(linkURL, depth+1))
        except aiohttp.ClientError:
            print(f"[{workerID} failed at {url =}]",
                  file=sys.stderr)
        finally:
            queue.task_done()


if __name__ == "__main__":
    asyncio.run(main(parse_args()))