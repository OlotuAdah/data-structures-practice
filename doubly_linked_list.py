class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.numOfNodes = 0
        self.head = None
        self.tail = None

    # insert in doubly linked list happens at the end
    # to allow manipulation of the linkedlist in O(1) running time
    def insert(self, data):
        self.numOfNodes += 1
        new_node = Node(data)
        if self.head is None:  # list is empty i.e. both head and tail should point to new_node
            self.head = new_node
            self.tail = new_node
        else:  # there is at least one itme in the list, so insert at the end
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node  # insertion happens at the end, so the tail must always be the new node

    def traverse_forward(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):
        actual_node = self.tail
        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.previous


if __name__ == '__main__':
    d_linked_list = DoublyLinkedList()
    d_linked_list.insert(9)
    d_linked_list.insert(8)
    d_linked_list.traverse_backward()
