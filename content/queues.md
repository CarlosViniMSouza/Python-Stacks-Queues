# Learning About the Types of Queues

A queue is an [abstract data type](https://en.wikipedia.org/wiki/Abstract_data_type) that represents a **sequence** of elements arranged according to a set of rules. In this section, you’ll learn about the most common types of queues and their corresponding element arrangement rules. At the very least, every queue provides operations for adding and removing elements in [constant time](https://en.wikipedia.org/wiki/Time_complexity#Constant_time) or O(1) using the [Big O notation](https://realpython.com/binary-search-python/#the-big-o-notation). That means both operations should be instantaneous regardless of the queue’s size.

Some queues may support other, more specific operations. It’s time to learn more about them!

## Queue: First-In, First-Out (FIFO)

The word *queue* can have different meanings depending on the context. However, when people refer to a queue without using any qualifiers, they usually mean a [FIFO queue](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics).

FIFO is short for *first-in*, *first-out*, which describes the flow of elements through the queue. Elements in such a queue will be processed on a first-come, first-served basis, which is how most real-life queues work. To better visualize the element movement in a FIFO queue.

Adding an element to the FIFO queue is commonly referred to as an **enqueue** operation, while retrieving one from it is known as a **dequeue** operation. Don’t confuse a dequeue operation with the [deque (double-ended queue)](https://realpython.com/queue-in-python/#deque-double-ended-queue) data type that you’ll learn about later!

**Note**: You can think of elements in a FIFO queue as cars stopping at a traffic light.

Another point worth noting about the queue depicted above is that it can grow without bounds as new elements arrive. Picture a checkout line stretching to the back of the store during a busy shopping season! In some situations, however, you might prefer to work with a **bounded queue** that has a fixed capacity known upfront.

The second strategy for dealing with incoming elements in a bounded FIFO queue lets you implement a basic **cache** that forgets the oldest element without considering how many times or how frequently you’ve accessed it. A FIFO cache works best when newer elements are more likely to be reused than older ones. For example, you can use the FIFO cache eviction strategy to forcefully log out users who logged in a long time ago regardless if they’re still active.

**Note**: For a brief comparison of other cache eviction strategies, head over to Caching in Python Using the LRU Cache Strategy.

## Stack: Last-In, First-Out (LIFO)