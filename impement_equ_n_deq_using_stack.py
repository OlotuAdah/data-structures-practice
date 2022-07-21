# the challenge is to implement enqueue and  dequeue using
# Stack (i.e. LIFO) instead of Queue (FIFO)

class Queue:
    def __init__(self):
        self.enqueue_stack = []  # for enqueue operation
        self.dequeue_stack = []  # for dequeue operation

    def enqueue(self, data):
        self.enqueue_stack.append(data)
        return self

    def dequeue(self):
        # empty stack
        if len(self.enqueue_stack) == 0 and len(self.dequeue_stack) == 0:
            raise Exception("Stack are empty!")
        # if the dequeue stack is empty, load it with the reverse of enqueue stack
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        # Otherwise, pop item in O(1) time complexity
        return self.dequeue_stack.pop()

    def traverse(self):
        for item in self.enqueue_stack:
            print(item)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(2).enqueue(3).traverse()

    print(q.dequeue())
