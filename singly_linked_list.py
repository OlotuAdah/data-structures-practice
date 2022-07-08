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
            # do this when list is Empty!'
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

    def remove_item(self, data_to_remove):
        if self.head is None:
            return -1

        if self.head.data == data_to_remove:
            self.head = self.head.next_node  # change head node to the next_node ref stored in head
            self.numNodes -= 1
            return 1
        actual_node = self.head
        previous_node = None
        while actual_node is not None and actual_node.data != data_to_remove:
            # If actual node (i.e. head node at first pass) matches the search item,
            # then previous_node will remain None
            previous_node = actual_node
            actual_node = actual_node.next_node
        if actual_node is None:
            # Search missed; data_to_remove not found in list
            return -1
        previous_node.next_node = actual_node.next_node
        self.numNodes -= 1  # reduce  item count
        return self

    # Time complexity is O(N)
    def traverse_list(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    # Time complexity is O(1)
    def get_list_size(self):
        return self.numNodes

    # Time complexity is O(1)
    def get_head(self):
        if self.head is not None:
            return self.head.data


if __name__ == '__main__':
    linkedList = LinkedList()
    linkedList.insert_start(6).insert_start(19).insert_start(90)
    print(f"====Before: { linkedList.get_list_size()}")
    linkedList.remove_end()
    print(f"====After: {linkedList.get_list_size()}")
    linkedList.traverse_list()

    # print(f'Num Nodes are: {linkedList.get_list_size()}')
    # print(f'First Node: {linkedList.get_head()}')
