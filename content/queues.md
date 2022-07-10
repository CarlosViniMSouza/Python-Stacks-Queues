# Learning About the Types of Queues

A queue is an [abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type) that represents a **sequence** of elements arranged according to a set of rules. In this section, you’ll learn about the most common types of queues and their corresponding element arrangement rules. At the very least, every queue provides operations for adding and removing elements in [constant time](https://en.wikipedia.org/wiki/Time_complexity#Constant_time) or O(1) using the [Big O notation](https://realpython.com/binary-search-python/#the-big-o-notation). That means both operations should be instantaneous regardless of the queue’s size.

Some queues may support other, more specific operations. It’s time to learn more about them!

<br>

## **Queue: First-In, First-Out (FIFO)**

The word *queue* can have different meanings depending on the context. However, when people refer to a queue without using any qualifiers, they usually mean a [FIFO queue](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics).

FIFO is short for *first-in*, *first-out*, which describes the flow of elements through the queue. Elements in such a queue will be processed on a first-come, first-served basis, which is how most real-life queues work. To better visualize the element movement in a FIFO queue.

Adding an element to the FIFO queue is commonly referred to as an **enqueue** operation, while retrieving one from it is known as a **dequeue** operation. Don’t confuse a dequeue operation with the [deque (double-ended queue)](https://realpython.com/queue-in-python/#deque-double-ended-queue) data type that you’ll learn about later!

<br>

**Note**: You can think of elements in a FIFO queue as cars stopping at a traffic light.

<br>


Another point worth noting about the queue depicted above is that it can grow without bounds as new elements arrive. Picture a checkout line stretching to the back of the store during a busy shopping season! In some situations, however, you might prefer to work with a **bounded queue** that has a fixed capacity known upfront.

The second strategy for dealing with incoming elements in a bounded FIFO queue lets you implement a basic **cache** that forgets the oldest element without considering how many times or how frequently you’ve accessed it. A FIFO cache works best when newer elements are more likely to be reused than older ones. For example, you can use the FIFO cache eviction strategy to forcefully log out users who logged in a long time ago regardless if they’re still active.

<br>

**Note**: For a brief comparison of other cache eviction strategies, head over to Caching in Python Using the LRU Cache Strategy.

<br>

## **Priority Queue**

A **priority queue** is different from those you’ve seen so far because it can’t store ordinary elements. Instead, each element must now have an associated priority to compare against other elements. The queue will maintain a **sorted order**, letting new elements join where necessary while shuffling the existing elements around if needed. When two elements are of equal priority, they’ll follow their insertion order.

<br>

**Note**: Make sure to choose a data type for your priorities whose values are comparable through the comparison operators, such as less than (<). For example, integers and timestamps would be fine, while complex numbers wouldn’t work for indicating priority because they don’t implement any relevant comparison operator.

<br>

You could use the priority queue to **sort a sequence** of elements by a given key or get the **top few elements**. However, that would be overkill because there are far more efficient [sorting algorithms](https://realpython.com/sorting-algorithms-python/) available. The priority queue is better suited for situations when elements can come and go dynamically. One such situation would be searching for the **shortest path** in a weighted graph using [Dijkstra’s algorithm](https://realpython.com/queue-in-python/#dijkstras-algorithm-using-a-priority-queue), which you’ll read about later.

<br>

**Note**: Even though the priority queue is conceptually a sequence, its most efficient implementation builds on top of the [heap data structure](https://realpython.com/python-heapq-module/), which is a kind of [binary tree](https://en.wikipedia.org/wiki/Binary_tree). Therefore, the terms heap and priority queue are sometimes used interchangeably.

<br>

## **Implementing Queues in Python**

Firstly, should you implement a queue yourself in Python? In most cases, the answer to that question will be a decisive no. The language comes with batteries included, and queues are no exception. In fact, you’ll discover that Python has an abundance of queue implementations suited to solving various problems.

That being said, trying to build something from scratch can be an invaluable learning experience. You might also get asked to provide a queue implementation during a [technical interview](https://realpython.com/python-coding-interview-tips/). So, if you find this topic interesting, then please read on. Otherwise, if you only seek to [use queues in practice](https://realpython.com/queue-in-python/#using-queues-in-practice), then feel free to skip this section entirely.

<br>

### Representing FIFO and LIFO Queues With a Deque

To represent a FIFO queue in the computer’s memory, you’ll need a [sequence](https://docs.python.org/3/glossary.html#term-sequence) that has O(1), or constant time, performance for the enqueue operation on one end, and a similarly efficient dequeue operation on the other end. As you already know by now, a deque or double-ended queue satisfies those requirements. Plus, it’s universal enough to adapt for a LIFO queue as well.

However, because coding one would be out of scope of this tutorial, you’re going to leverage Python’s [deque collection](https://realpython.com/python-deque/) from the standard library.

<br>

### Building a Queue Data Type

**Note**: You’ll have a closer look at the built-in queue module in a later section devoted to thread-safe queues in Python.

<br>

Because you want your custom FIFO queue to support at least the enqueue and dequeue operations, go ahead and write a bare-bones Queue class that’ll delegate those two operations to `deque.append()` and `deque.popleft()` methods, respectively:

`see the code in path: python/deque.py`

As expected, the enqueued elements come back to you in their original order. If you want, you may improve your class by making it [iterable](https://docs.python.org/3/glossary.html#term-iterable) and able to report its length and optionally accept initial elements:

```python
# deque.py

from collections import deque


class Queue:
    def __init__(self, *elements) -> None:
        self._elements = deque(elements)

    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
```

A deque takes an optional iterable, which you can provide through a varying number of positional arguments, *elements, in your initializer method. By implementing the special `.__iter__()` method, you’ll make your class instances usable in a [for loop](https://realpython.com/python-for-loop/), while implementing `.__len__()` will make them compatible with the len() function. The `.__iter__()` method above is an example of a [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator), which [yields](https://realpython.com/introduction-to-python-generators/) elements [lazily](https://en.wikipedia.org/wiki/Lazy_evaluation).

<br>

**Note**: The implementation of `.__iter__()` causes your custom queue to reduce its size by dequeuing elements from itself as you iterate over it.

<br>

## **Representing Priority Queues With a Heap**

The last queue that you’ll implement in this tutorial will be a priority queue. Unlike a stack, the priority queue can’t extend the `Queue` class defined earlier, because it doesn’t belong to the same type hierarchy. The order of elements in a FIFO or LIFO queue is determined solely by the elements’ time of arrival. In a priority queue, it’s an element’s priority and the insertion order that together determine the ultimate position within the queue.

There are many ways to implement a priority queue, such as:

&nbsp; &nbsp; ° An **unordered list** of elements and their priorities, which you search through every time before dequeuing the element with the highest priority

&nbsp; &nbsp; ° An **ordered list** of elements and their priorities, which you sort every time you enqueue a new element

&nbsp; &nbsp; ° An **ordered list** of elements and their priorities, which you keep sorted by finding the right spot for a new element using [binary search](https://realpython.com/binary-search-python/)

&nbsp; &nbsp; ° A **binary tree** that maintains the heap [invariant](https://en.wikipedia.org/wiki/Invariant_(mathematics)#Invariants_in_computer_science) after the enqueue and dequeue operations

Looking up an element in an unordered list has `O(n) time complexity`. Sorting the entire queue would be even more expensive, especially when exercised often. Python’s `list.sort()` method employs an algorithm called [Timsort](https://en.wikipedia.org/wiki/Timsort), which has `O(n log(n))` worst-case time complexity. Inserting an element with [`bisect.insort()`](https://realpython.com/binary-search-python/#using-the-bisect-module) is slightly better because it can take advantage of an already sorted list, but the gain is offset by the slow insertion that follows.

Fortunately, you can be smart about keeping the elements sorted in a priority queue by using a **heap data structure** under the hood.

<br>

| Implementation                | Enqueue     | Dequeue   |
|-------------------------------|-------------|-----------|
| Find Max on Dequeue	          | O(1)        | O(n)      |
| Sort on Enqueue	              | O(n log(n)) | O(1)      |
| Bisect and Insert on Enqueue  | O(n)        | O(1)      |
| Push onto a Heap on Enqueue		 | O(log(n))   | O(log(n)) |

<br>

The heap has the best overall performance for large data volumes. Although using the [bisection method](https://en.wikipedia.org/wiki/Bisection_method) to find the right spot for a new element is O(log(n)), the actual insertion of that element is O(n), making it less desirable than a heap.

Python has the `heapq` module, which conveniently provides a few functions that can turn a regular list into a heap and manipulate it efficiently. The two functions that’ll help you build a priority queue are:

&nbsp; &nbsp; 1 - `heapq.heappush()`

&nbsp; &nbsp; 2 - `heapq.heappop()`

When you push a new element onto a non-empty heap, it’ll end up in the right spot, maintaining the heap invariant.

`see the file in python/heap.py`

<br>

## **Building a Priority Queue Data Type**

Imagine you were building software for an automotive company. Modern vehicles are practically computers on wheels, which leverage a [controller area network (CAN)](https://en.wikipedia.org/wiki/CAN_bus) bus to broadcast messages about various events going on in your car, such as unlocking the doors or inflating an airbag. Clearly, some of those events are more important than others and should be prioritized accordingly.

It’s okay to miss a faulty headlight message or wait a little longer for the audio volume level to go down. However, when you press the brake pedal, you expect it to have an immediate effect because it’s a safety-critical subsystem. Each message has a priority in the CAN bus protocol, which tells the intermediate units whether they should relay the message further or disregard it completely.

```python
class PriorityQueue:
    def __init__(self) -> None:
        self._elements = []

    def pushElementPriority(self, priority, value):
        heappush(self._elements, (priority, value))

    def popElementPriority(self):
        return heappop(self._elements)
```

It’s a basic priority queue implementation, which defines a heap of elements using a Python list and two methods that manipulate it. The `.pushElementsPriority()` method takes two arguments, a priority and a corresponding value, which it then wraps in a tuple and pushes onto the heap using the heapq module. Notice that the priority comes before the value to take advantage of how Python compares tuples.

```python
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
```

You defined three priority levels: critical, important, and neutral. Next, you instantiated a priority queue and used it to enqueue a few messages with those priorities. However, instead of dequeuing the message with the highest priority, you got a tuple corresponding to the message with the *lowest* priority.
