# Deque: Double-Ended Queue

A [double-ended queue](https://en.wikipedia.org/wiki/Double-ended_queue) or **deque** (pronounced *deck*) is a more generic data type that combines and extends the ideas behind the stack and the queue. It allows you to enqueue or dequeue elements from both ends in constant time at any given moment. Therefore, a deque can work as a *FIFO or a LIFO queue*, as well as anything in between and beyond.

Most elements generally follow one direction by joining the queue on the **right** and leaving it on the **left**, just like in a plain *FIFO queue*. However, some privileged elements are allowed to join the queue from the left end, while the last element can leave the queue through the opposite end.

Adding an element to a **bounded deque** that has already reached its full capacity will overwrite the element currently located at the opposite end. That feature might be handy for isolating the first few or the last few elements from a sequence.

Most deques support two additional operations called **rotate left** and **rotate right**, which shift the elements a specified number of places in one or the other direction in a circular fashion. Because the deque’s size remains unchanged, elements that would stick out get wrapped around at the ends, as in an[ analog car odometer](https://upload.wikimedia.org/wikipedia/commons/5/53/Odometer_rollover.jpg):

When rotated right, the last element in the deque becomes first. On the other hand, when rotated left, the first element becomes the last one. Perhaps you could imagine this process more easily by arranging the deque’s elements in a circle so that both ends meet. Then, rotating right and left would correspond to a clockwise and counterclockwise rotation, respectively.

Rotations, combined with the deque’s core capabilities, open up interesting possibilities. For example, you could use a deque to implement a [load balancer](https://en.wikipedia.org/wiki/Load_balancing_(computing)) or a task scheduler working in a [round-robin](https://en.wikipedia.org/wiki/Round-robin_scheduling) fashion. In a [GUI application](https://realpython.com/learning-paths/python-gui-programming/), you could use a deque to store recently opened files, allow a user to **undo and redo** their actions, or let the user navigate back and forth through their **web browsing history**.
