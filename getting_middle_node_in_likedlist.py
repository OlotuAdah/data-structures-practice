#  !!! interview question

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.numNodes = 0
        self.head = None

    #  # Time complexity is O(1)
    def insert_start(self, data):
        self.numNodes += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            # points the new node to the existing node (i.e. self.node in this case)
            new_node.next_node = self.head
            # NB: self.head is always the first node. Now, make the new_node the first node
            self.head = new_node
        return self  # Just to enable chaining function call

    # time complexity is O(N)
    def insert_end(self, data):
        self.numNodes += 1
        new_node = Node(data)
        actual_node = self.head

        try:
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node
            return self
        except AttributeError:
            # do this when list is Empty!, i.e. actual_node is none,
            # and None Type has next_node property (Error thrown )
            self.head = new_node
            return self

    def remove_start(self):
        if self.head is not None:
            self.numNodes -= 1
            second_node = self.head.next_node
            # print(self.head.next_node.data)
            self.head = second_node
            # del first_node

    # Time complexity is O(N)
    def remove_end(self):
        # if self.head is not None:
        self.numNodes -= 1
        actual_node = self.head
        while actual_node is not None:
            actual_node = actual_node.next_node
        del actual_node

    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head
        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node
        return slow_pointer.data

    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    def reverse_list(self):
        current_node = self.head
        next_node = None
        previous_node = None
        while current_node is not None:
            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node


if __name__ == '__main__':
    linkedList = LinkedList().insert_end(1).insert_end(2).insert_end(3).insert_end(4).insert_end(5).insert_end(6)
    # print(linkedList.get_middle_node())
    linkedList.traverse_list()
    linkedList.reverse_list()
    print("===================")
    linkedList.traverse_list()

# 1, 2, 3, 4, 5, 6
# 6, 5, 4, 3, 2, 1
