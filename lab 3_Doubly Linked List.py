class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class my_doubly_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None

    def delete_at_beginning(self):
        if (self.head == None):
            return
        else:
            if (self.head != self.tail):
                self.head = self.head.next
                self.head.previous = None
            else:
                self.head = self.tail = None

    def delete_at_end(self):
        if (self.head == None):
            return
        else:
            if (self.head != self.tail):
                self.tail = self.tail.previous
                self.tail.next = None
            else:
                self.head = self.tail = None

    def insert_at_beginning(self, data):
        newNode = Node(data)

        if (self.head == None):
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.head.previous = newNode
            newNode.next = self.head
            newNode.previous = None
            self.head = newNode

    def insert_at_end(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = self.tail = newNode
            self.head.previous = None
            self.tail.next = None
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.tail.next = None

    def traverse(self):
        current = self.head
        if (self.head == None):
            print("List is empty")
            return
        while (current != None):
            print(current.data, end = '  ')
            current = current.next
        print()

List = my_doubly_list()
List.add_node(2)
List.add_node(23)
List.add_node(57)
List.add_node(97)
List.add_node(86)
List.add_node(29)
print("Created linked list:")
List.traverse()

List.delete_at_beginning()
List.delete_at_end()
print("\nLinked List after deletion at the start and end :")
List.traverse()

List.insert_at_beginning(27)
List.insert_at_beginning(30)
List.insert_at_end(10)
List.insert_at_end(19)
print("\nLinked List after insertion of 27 and 30 at start and 10 and 19 at the end :")
List.traverse()
