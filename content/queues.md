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

</br>

Another point worth noting about the queue depicted above is that it can grow without bounds as new elements arrive. Picture a checkout line stretching to the back of the store during a busy shopping season! In some situations, however, you might prefer to work with a **bounded queue** that has a fixed capacity known upfront.

The second strategy for dealing with incoming elements in a bounded FIFO queue lets you implement a basic **cache** that forgets the oldest element without considering how many times or how frequently you’ve accessed it. A FIFO cache works best when newer elements are more likely to be reused than older ones. For example, you can use the FIFO cache eviction strategy to forcefully log out users who logged in a long time ago regardless if they’re still active.

<br>

**Note**: For a brief comparison of other cache eviction strategies, head over to Caching in Python Using the LRU Cache Strategy.

</br>

## **Priority Queue**

A **priority queue** is different from those you’ve seen so far because it can’t store ordinary elements. Instead, each element must now have an associated priority to compare against other elements. The queue will maintain a **sorted order**, letting new elements join where necessary while shuffling the existing elements around if needed. When two elements are of equal priority, they’ll follow their insertion order.

<br>

**Note**: Make sure to choose a data type for your priorities whose values are comparable through the comparison operators, such as less than (<). For example, integers and timestamps would be fine, while complex numbers wouldn’t work for indicating priority because they don’t implement any relevant comparison operator.

</br>

You could use the priority queue to **sort a sequence** of elements by a given key or get the **top few elements**. However, that would be overkill because there are far more efficient [sorting algorithms](https://realpython.com/sorting-algorithms-python/) available. The priority queue is better suited for situations when elements can come and go dynamically. One such situation would be searching for the **shortest path** in a weighted graph using [Dijkstra’s algorithm](https://realpython.com/queue-in-python/#dijkstras-algorithm-using-a-priority-queue), which you’ll read about later.

<br>

**Note**: Even though the priority queue is conceptually a sequence, its most efficient implementation builds on top of the [heap data structure](https://realpython.com/python-heapq-module/), which is a kind of [binary tree](https://en.wikipedia.org/wiki/Binary_tree). Therefore, the terms heap and priority queue are sometimes used interchangeably.

</br>
