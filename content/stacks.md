# Stack: Last-In, First-Out (LIFO)

A stack is a more specialized queue, also known as a LIFO or **last-in**, **first-out** queue. It works almost exactly like a regular queue, except that elements must now join and leave it through only one end called the **top** of the stack. The name *top* reflects the fact that real-world stacks tend to be vertical. A pile of plates in the kitchen sink is an example of a stack.

When the dishwasher is full, employees will **push** their dirty plates *on the top of the stack* after having a meal. Once there are no more clean plates in the cabinet, a hungry employee will have to **pop** the last dirty plate from the top of the stack and clean it with a sponge before microwaving their lunch.

Even though the LIFO queue above is oriented horizontally, it preserves the general idea of a stack. New elements grow the stack by joining it only on the right end, as in the previous examples. This time, however, only the last element pushed onto the stack can leave it. The rest must wait until there are no more elements that have joined the stack later.

Stacks are widely used in computing for various purposes. Perhaps the most familiar context for a programmer is the [call stack](https://en.wikipedia.org/wiki/Call_stack) containing the functions in the order they were called. Python will reveal this stack to you through a [traceback](https://realpython.com/python-traceback/) in case of an unhandled [exception](https://realpython.com/python-exceptions/). It’s usually a **bounded stack** with a limited capacity, which you’ll find out about during a [stack overflow error](https://en.wikipedia.org/wiki/Stack_buffer_overflow) caused by too many [recursive](https://realpython.com/python-recursion/) calls.

<br>

**Note**: When you replace the stack, or LIFO queue, with a FIFO queue in the DFS algorithm and make a few minor tweaks, then you’ll get the breadth-first search (BFS) algorithm almost for free!

</br>

## **Building a Stack Data Type**
Building a [stack](https://realpython.com/how-to-implement-python-stack/) data type is considerably more straightforward because you’ve already done the bulk of the hard work. Since most of the implementation will remain the same, you can extend your Queue class using [inheritance](https://realpython.com/inheritance-composition-python/) and override the `.dequeue()` method to remove elements from the top of the stack:

```python
# deque.py

class Stack(Queue):
    def popElement(self):
        return self._elements.pop()
```

<br>

**Note**: In this tutorial, you use inheritance as a convenient mechanism to reuse code. However, the current class relationship isn’t semantically correct, because a stack isn’t a subtype of a queue. You could just as well define the stack first and let the queue extend it. In the real world, you should probably make both classes inherit from an [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class) because they share the same interface.

</br>

## **Representing Priority Queues With a Heap**
