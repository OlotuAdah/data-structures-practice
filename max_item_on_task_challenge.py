# Challenge is to develop a get max method that could get max item on a stack
# in O(1) running time complexity
class Stack:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []

    def push(self, data):
        if len(self.main_stack) < 1:  # stack is empty, append data to both main and max stack
            self.main_stack.append(data)
            self.max_stack.append(data)
            return self
        else:  # there is at least one item on the stack
            if self.max_stack[-1] > data:
                self.main_stack.append(data)
                self.max_stack.append(self.max_stack[-1])
                return self
            else:
                self.main_stack.append(data)
                self.max_stack.append(data)
                return self

    def pop(self):
        del self.max_stack[-1]
        rm_item = self.main_stack[-1]
        del self.main_stack[-1]
        return rm_item

    # O(1) running time complexity
    def get_max_item_on_stack(self):
        return self.max_stack[-1]

    def traverse_max_stack(self):
        for item in self.max_stack:
            print(item)

    def traverse_main_stack(self):
        for item in self.main_stack:
            print(item)


if __name__ == '__main__':
    stack = Stack()
    stack.push(10).push(89).push(25).push(8).push(4)
    print(stack.get_max_item_on_stack())
    #
    print("==========Max Stack=====")
    stack.traverse_max_stack()
    print("==========Main Stack======")
    stack.traverse_main_stack()
