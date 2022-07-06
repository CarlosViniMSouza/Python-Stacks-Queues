![queues-stacks-article](https://files.realpython.com/media/How-to-Implement-A-Queue-in-Python_Watermarked.993460fe2ffc.jpg)

# [Python Stacks, Queues, and Priority Queues in Practice](https://realpython.com/queue-in-python/)

```
Table of Contents

° Learning About the Types of Queues
   ° Queue: First-In, First-Out (FIFO)
   ° Stack: Last-In, First-Out (LIFO)
   ° Deque: Double-Ended Queue
   ° Priority Queue: Sorted From High to Low

° Implementing Queues in Python
   ° Representing FIFO and LIFO Queues With a Deque
   ° Building a Queue Data Type
   ° Building a Stack Data Type
   ° Representing Priority Queues With a Heap
   ° Building a Priority Queue Data Type
   ° Handling Corner Cases in Your Priority Queue
   ° Refactoring the Code Using a Mixin Class

° Using Queues in Practice
   ° Sample Data: Road Map of the United Kingdom
   ° Object Representation of the Cities and Roads
   ° Breadth-First Search Using a FIFO Queue
   ° Shortest Path Using Breadth-First Traversal
   ° Depth-First Search Using a LIFO Queue
   ° Dijkstra’s Algorithm Using a Priority Queue

° Using Thread-Safe Queues
   ° queue.Queue
   ° queue.LifoQueue
   ° queue.PriorityQueue

° Using Asynchronous Queues
   ° asyncio.Queue
   ° asyncio.LifoQueue
   ° asyncio.PriorityQueue

° Using multiprocessing.Queue for Interprocess Communication (IPC)
   ° Reversing an MD5 Hash on a Single Thread
   ° Distributing Workload Evenly in Chunks
   ° Communicating in Full-Duplex Mode
   ° Killing a Worker With the Poison Pill
   ° Analyzing the Performance of Parallel Execution

° Integrating Python With Distributed Message Queues
   ° RabbitMQ: pika
   ° Redis: redis
   ° Apache Kafka: kafka-python3

° Conclusion
```

Queues are the backbone of numerous algorithms found in games, artificial intelligence, satellite navigation, and task scheduling. They’re among the top **abstract data types** that computer science students learn early in their education. At the same time, software engineers often leverage higher-level **message queues** to achieve better scalability of a [microservice architecture](https://realpython.com/python-microservices-grpc/). Plus, using queues in Python is simply fun!

Python provides a few **built-in flavors of queues** that you’ll see in action in this tutorial. You’re also going to get a quick primer on the **theory of queues** and their types. Finally, you’ll take a look at some **external libraries** for connecting to popular message brokers available on major cloud platform providers.