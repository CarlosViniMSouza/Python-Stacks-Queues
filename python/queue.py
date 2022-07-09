"""
This class merely wraps a collections.deque instance and calls it ._elements.
The leading underscore in the attribute's name indicates an internal bit of implementation,
which only the class should access and modify.

Such fields are sometimes called private because they're not supposed to be visible outside the class body.
"""

from collections import deque


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
