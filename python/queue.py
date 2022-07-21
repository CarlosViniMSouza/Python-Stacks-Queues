"""
This class merely wraps a collections.deque instance and calls it ._elements.
The leading underscore in the attribute's name indicates an internal bit of implementation,
which only the class should access and modify.

Such fields are sometimes called private because they're not supposed to be visible outside the class body.
"""

from itertools import count
from collections import deque
from heapq import heappop, heappush
from dataclasses import dataclass
from itertools import count


class IterableMixin:
    def __len__(self):
        return len(self._element)

    def __iter__(self):
        while len(self) > 0:
            yield self.popElement()


class Queue(IterableMixin):
    def __init__(self, *element) -> None:
        self._element = deque(element)

    def __len__(self) -> int:
        return len(self._element)

    def __iter__(self):
        if len(self._element) > 0:
            yield self.popElement()

    def addElement(self, data):
        self._element.append(data)

    def popElement(self):
        self._element.popleft()


class Stack(Queue):
    def popElement(self):
        return self._element.pop()


class PriorityQueue(IterableMixin):
    def __init__(self) -> None:
        self._elements = []
        self._counter = count()

    def pushElementPriority(self, priority, value):
        element = (priority, next(self._counter), value)
        return heappush(self._elements, element)

    def popElementPriority(self):
        return heappop(self._elements)[-1]


class LifoQueue:
    pass


@dataclass
class Message:
    event: str


wipers = Message("Windshield wipers turned on")
hazard = Message("Hazard lights turned on")
test = Message("This message it´s not Important")

messages = PriorityQueue()

NEUTRAL = 1
IMPORTANT = 2
CRITICAL = 3

messages.pushElementPriority(IMPORTANT, "Windshield wipers turned on")
messages.pushElementPriority(NEUTRAL, "Radio station turned in")
messages.pushElementPriority(CRITICAL, "Brake pedal depressed")
messages.pushElementPriority(IMPORTANT, "Hazard lights turned on")

print(messages.popElementPriority())
# output: (1, 'Radio station turned in')

print(messages.popElementPriority())
# output: (2, 'Hazard lighhts turned on')
