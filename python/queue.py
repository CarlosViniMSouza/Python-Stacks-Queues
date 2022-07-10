"""
This class merely wraps a collections.deque instance and calls it ._elements.
The leading underscore in the attribute's name indicates an internal bit of implementation,
which only the class should access and modify.

Such fields are sometimes called private because they're not supposed to be visible outside the class body.
"""

from collections import deque
from heapq import heappop, heappush


class Queue:
    def __init__(self, *elements) -> None:
        self._elements = deque(elements)

    def __len__(self) -> int:
        return len(self._elements)

    def __iter__(self):
        if len(self._elements) > 0:
            yield self.popElement()

    def addElement(self, data):
        self._elements.append(data)

    def popElement(self):
        self._elements.popleft()


class Stack(Queue):
    def popElement(self):
        return self._elements.pop()


class PriorityQueue:
    def __init__(self) -> None:
        self._elements = []

    def pushElementPriority(self, priority, value):
        heappush(self._elements, (priority, value))

    def popElementPriority(self):
        return heappop(self._elements)


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
