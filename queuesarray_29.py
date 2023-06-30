# implement queue data structure in array

# implement a queue data structure in array
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def size(self):
        return len(self.queue)

# Example usage
queue = Queue()
queue.enqueue(20)
queue.enqueue(40)
queue.enqueue(60)
print("The Queue size:", queue.size())
print("The Queue peek:", queue.peek())
print("The Dequeued item:", queue.dequeue())
print("The Queue size:", queue.size())