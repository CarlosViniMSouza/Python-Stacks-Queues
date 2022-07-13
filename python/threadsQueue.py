# (venv) $ python -m pip install rich

import argparse
from itertools import zip_longest

from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

from queue import PriorityQueue, Queue, LifoQueue

class View:
    def __init__(self, buffer, producers, consumers):
        self.buffer = buffer
        self.producers = producers
        self.consumers = consumers

    def animate(self):
        with Live(
            self.render(), screen=True, refresh_per_second=5
        ) as live:
            while True:
                live.update(self.render())

    def render(self):
        match self.buffer:
            case PriorityQueue():
                title = "Priority Queue Class"
                products = map(str, reversed(list(self.buffer.queue)))

            case LifoQueue():
                title = "Stack Class"
                products = list(self.buffer.queue)

            case Queue():
                title = "Queue Class"
                products = reversed(list(self.buffer.queue))

            case _:
                title = "not defined"
                products = "not defined"

        rows = [Panel(f"[bold]{title}:[/] {', '.join(products)}",
                  width=80)]

        pairs = zip_longest(self.producers, self.consumers)

        for i, (producer, consumer) in enumerate(pairs, 1):
            left_panel = self.panel(producer, f"Producer {i}")
            right_panel = self.panel(consumer, f"Consumer {i}")

            rows.append(Columns([left_panel, right_panel], width=40))

        return Group(*rows)

    def panel(self, worker, title):
        if worker is None:
            return "Empty"

        padding = " " * int(29/100 * worker.progress)
        align = Align(
            padding + worker.state,
            align="left",
            vertical="middle"
        )

        return Panel(align, height=5, title=title)


queueTypes = {
    "FIFO": Queue,
    "LIFO": LifoQueue,
    "HEAP": PriorityQueue
}

def main(args):
    buffer = queueTypes[args.queue]()

def parseARGS():
    parser = argparse.ArgumentParser()

    parser.add_argument("-q", "--queue", choices=queueTypes, default="FIFO")
    parser.add_argument("-p", "--producers", type=int, default=3)
    parser.add_argument("-c", "--consumers", type=int, default=2)
    parser.add_argument("-ps", "--prod-speed", type=int, default=1)
    parser.add_argument("-cs", "--cons-speed", type=int, default=1)

    return parser.parse_args()

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

if __name__ == "__main__":
    try:
        main(parseARGS())
    except KeyboardInterrupt:
        pass
