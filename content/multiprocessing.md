## Using multiprocessing.Queue for Interprocess Communication (IPC)

So far, you’ve looked into queues that can only help in scenarios with strictly I/O-bound tasks, whose progress doesn’t depend on the available computational power. On the other hand, the traditional approach to running [CPU-bound](https://en.wikipedia.org/wiki/CPU-bound) tasks on multiple CPU cores in parallel with Python takes advantage of cloning the interpreter process. Your operating system provides the [interprocess communication (IPC)](https://en.wikipedia.org/wiki/Inter-process_communication) layer for sharing data across these processes.

You’ll only find the FIFO queue in the multiprocessing module, which comes in three variants:

1. multiprocessing.Queue

2. multiprocessing.SimpleQueue

3. multiprocessing.JoinableQueue

They’re all modeled after the thread-based *queue.Queue* but differ in the level of completeness. The *JoinableQueue* extends the *multiprocessing.Queue* class by adding `.task_done()` and `.join()` methods, allowing you to wait until all enqueued tasks have been processed. If you don’t need this feature, then use *multiprocessing.Queue* instead. *SimpleQueue* is a separate, significantly streamlined class that only has `.get()`, `.put()`, and `.empty()` methods.

To see a hands-on example of *multiprocessing.Queue*, you’ll simulate a computationally intensive task by trying to reverse an [MD5](https://en.wikipedia.org/wiki/MD5) hash value of a short text using the [brute-force](https://en.wikipedia.org/wiki/Brute-force_attack) approach. While there are better ways to solve this problem, both [algorithmically](https://en.wikipedia.org/wiki/Dictionary_attack) and [programmatically](https://docs.python.org/3/library/multiprocessing.html#using-a-pool-of-workers), running more than one process in parallel will let you noticeably reduce the processing time.
