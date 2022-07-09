"""
I decided import the Queue class for here with an objective:

- improve the making of our Stack class (but i allow the tutorial)
"""

from queue import Queue


class Stack(Queue):
    def popElement(self):
        return self._elements.pop()
