# Using Thread-Safe Queues

Now suppose you’ve written a program with more than one flow of execution. Beyond being a valuable algorithmic tool, queues can help abstract away [concurrent](https://realpython.com/python-concurrency/) access to a shared resource in a [multithreaded](https://realpython.com/intro-to-python-threading/) environment without the need for explicit locking. Python provides a few **synchronized queue** types that you can safely use on multiple threads to facilitate communication between them.

In this section, you’re going to implement the classic [multi-producer, multi-consumer](https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem) problem using Python’s [thread-safe](https://en.wikipedia.org/wiki/Thread_safety) queues.

All parameters are optional and have sensible defaults. When you run this script, you’ll see an animated simulation of the producer and consumer threads communicating over a synchronized queue:

![img-painel-queues](https://files.realpython.com/media/queue_fifo.4bfb28b845b0.png)

The script uses the Rich library, which you’ll need to install into your virtual environment first:

```shell
(venv) $ python -m pip install rich
```

`see the file in: python/threadingQueue.py`

Notice the use of [structural pattern matching](https://realpython.com/python310-new-features/#structural-pattern-matching) to set the title and products based on the queue type. You’ll create an instance of the view and call its `.animate()` method once the producers and consumers are in place.

Next up, you’ll define the producer and consumer classes, and connect the pieces together.

## queue.Queue