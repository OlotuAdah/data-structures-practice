# LIFO: "Last In First Out" data structure.
# It's an abstract data structure that can be implemented with either array or linkedlist

class Stack:
    def __init__(self):
        self.stack = []

    # insert item to the stack
    def push(self, data):
        self.stack.append(data)
        return self  # just for chaining multiple push functions

    # O(1)
    def pop(self):  # remove and return last item on the list
        if self.stack_size() < 1:
            return -1
        last_item = self.stack[-1]
        del self.stack[-1]
        return last_item

    def peek(self):
        if self.stack_size() < 1:
            return -1
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []  # empty array returns true, otherwise false

    def stack_size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1).push(2).push(3).push(4).push(89)
    print(stack.stack_size())
    print(stack.pop())
    print(stack.peek())
    print(stack.stack_size())
