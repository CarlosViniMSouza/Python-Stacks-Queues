# before: (venv) $ python -m pip install rich

import argparse
from pydoc import importfile
import threading
from time import sleep
from enum import IntEnum
from itertools import zip_longest
from random import randint, choice
from dataclasses import dataclass, field
from regex import P

from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

from queue import PriorityQueue, Queue, LifoQueue


class Worker(threading.Thread):
    def __init__(self, speed, buffer):
        super().__init__(self, speed, buffer)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0

    @property
    def stateWork(self):
        if self.working:
            return f"{self.product} ({self.progress}%)"
        return ":zzz: IDLE"

    def simulateIDLE(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 5))

    def simulateWork(self):
        self.working = True
        self.progress = 0
        delay = randint(1, 1 + 20 // self.speed)

        for _ in range(100):
            sleep(delay/100)
            self.progress += 1


class View:
    def __init__(self, buffer, producers, consumers):
        self.buffer = buffer
        self.producers = producers
        self.consumers = consumers

    def animate(self):
        with Live(
            self.render(),
            screen=True,
            refresh_per_second=10
        ) as live:
            while True:
                live.update(self.render())

    def render(self):
        match self.buffer:
            case PriorityQueue():
                title = "Priority Queue Class"
                products = map(
                    str,
                    reversed(list(self.buffer.queue))
                )

            case LifoQueue():
                title = "Stack Class"
                products = list(self.buffer.queue)

            case Queue():
                title = "Queue Class"
                products = reversed(list(self.buffer.queue))

            case _:
                title = products = "not defined"

        rows = [
            Panel(
                f"[bold]{title}:[/] {', '.join(products)}",
                width=85
            )]

        pairs = zip_longest(
            self.producers,
            self.consumers
        )

        for i, (producer, consumer) in enumerate(pairs, 1):
            leftPanel = self.panel(
                producer,
                f"Producer {i}"
            )
            rightPanel = self.panel(
                consumer,
                f"Consumer {i}"
            )
            rows.append(Columns([
                leftPanel,
                rightPanel
            ],
                width=40))

        return Group(*rows)

    def panel(self, worker, title):
        if worker is None:
            return ""

        padding = " " * int(30/100 * worker.progress)
        align = Align(
            padding + worker.state,
            align="left",
            vertical="middle"
        )

        return Panel(align, height=5, title=title)


class Producer(Worker):
    def __init__(self, speed, buffer, products):
        super().__init__(speed, buffer)
        self.products = products

    def runSimulate(self):
        while True:
            self.product = choice(self.products)
            self.simulateWork()
            self.buffer.put(self.product)
            self.simulateIDLE()

    """
    The .runSimulate() method is where all the magic happens!
    """


class Consumer(Worker):
    def runSimulate(self):
        self.product = self.buffer.get()
        self.simulateWork()
        self.buffer.taskDone()
        self.simulateIDLE()

    """
    It also works in an infinite loop, waiting for a product to appear in the queue.
    """


@dataclass(order=True)
class Product:
    priority: int
    label: str = field(compare=False)

    def __str__(self):
        return self.label


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1


queueTypes = {
    "FIFO": Queue,
    "LIFO": LifoQueue,
    "HEAP": PriorityQueue
}

PRODUCTS = (
    ":balloon:",
    ":cookie:",
    ":crystal_ball:",
    ":diving_mask:",
    ":flashlight:",
    ":gem:",
    ":gift:",
    ":kite:",
    ":party_popper:",
    ":postal_horn:",
    ":ribbon:",
    ":rocket:",
    ":teddy_bear:",
    ":thread:",
    ":yo-yo:",
)

prioriPRODUCTS = (
    Product(Priority.HIGH, ":1st_place_medal:"),
    Product(Priority.MEDIUM, ":2nd_place_medal:"),
    Product(Priority.LOW, ":3rd_place_medal:"),
)


def main(args):
    buffer = queueTypes[args.queue]()
    products = prioriPRODUCTS if args.queue == "heap" else PRODUCTS
    producers = [
        Producer(
            args.producer_speed,
            buffer,
            products
        )
        for _ in range(args.producers)
    ]

    consumers = [
        Consumer(
            args.consumer_speed,
            buffer
        ) for _ in range(args.consumers)
    ]

    for producer in producers:
        producer.start()

    for consumer in consumer:
        consumer.start()

    view = View(buffer, producers, consumers)
    view.animate()


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-q", "--queue", choices=queueTypes, default="FIFO")
    parser.add_argument("-p", "--producers", type=int, default=3)
    parser.add_argument("-c", "--consumers", type=int, default=2)
    parser.add_argument("-ps", "--prod-speed", type=int, default=1)
    parser.add_argument("-cs", "--cons-speed", type=int, default=1)

    return parser.parse_args()


if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        pass
