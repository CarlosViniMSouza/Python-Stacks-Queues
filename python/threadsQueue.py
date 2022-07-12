# (venv) $ python -m pip install rich

import argparse
from queue import PriorityQueue, Queue, LifoQueue

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

if __name__ == "__main__":
    try:
        main(parseARGS())
    except KeyboardInterrupt:
        pass
