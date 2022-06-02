class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_element_by_value(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None
    def traverse(self):
        temp = self.head
        while (temp):
            print(" %d" % (temp.data), end = ' '),
            temp = temp.next

llist = LinkedList()
llist.insert_at_beginning(2)
llist.insert_at_beginning(5)
llist.insert_at_beginning(7)
llist.insert_element_by_value(6)
llist.insert_element_by_value(4)
print("Created linked list:")
llist.traverse()
llist.deleteNode(7)
llist.deleteNode(5)
print("\nLinked List after Deletion of 7 and 5:" )
llist.traverse()
