# FIFO: "First In First Out" data structure.
# Like Stack, it's an abstract data structure that can be implemented with either array or linkedlist
# Several Applications in OS and thread management (multithreading)
# Graph algo like BFS (Breadth-First Search) rely heavily on them
# CPU Scheduling, et ce tera.

class Queue:
    def __init__(self):
        self.queue = []

    # O(1)
    def is_empty(self):
        return self.queue == []

    # O(1)
    def enqueue(self, data):
        self.queue.append(data)
        return self

    # O(N) running time complexity. Solved by using Doubly LinkedList instead of array
    def dequeue(self):
        if self.size_queue() < 1:
            return -1
        data = self.queue[0]  # FIFO: so returns first item inserted
        del self.queue[0]  # del first element, array needs to reindex
        return data

    def peek(self):
        if self.size_queue() < 1:
            return -1
        return self.queue[0]

    def size_queue(self):
        return len(self.queue)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(8).enqueue(5).enqueue(6)
    print(queue.size_queue())
    print(queue.dequeue())
    print(queue.size_queue())
