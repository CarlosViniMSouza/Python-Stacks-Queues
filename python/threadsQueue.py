# (venv) $ python -m pip install rich

import threading
import argparsei
from random import randint
from time import sleep
from queue import PriorityQueue, Queue, LifoQueue


class Worker(threading.Thread):
    def __init__(self, speed, buffer):
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
        self.progress  0

        sleep(randint(1, 3))

    def simulateWork(self):
        self.working = True
        self.progress = 0
        delay = randint(1, 1 + 10 // self.speed)

        for _ in range(100):
            sleep(delay/100)
            self.progress += 1


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
