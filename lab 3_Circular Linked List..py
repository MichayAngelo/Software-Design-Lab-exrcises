class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class my_circular_list:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head

    def add_node(self, data):
        newNode = Node(data)
        if self.head.data is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.tail.next = self.head

    def insert_at_beginning(self, my_data):
        ptr_1 = Node(my_data)
        temp = self.head
        ptr_1.next = self.head

        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr_1
        else:
            ptr_1.next = ptr_1
        self.head = ptr_1

    def insert_at_end(self, my_data):
        new_node = Node(my_data)
        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def delete_start(self):
        if (self.head == None):
            return
        else:
            if (self.head != self.tail):
                self.head = self.head.next;
                self.tail.next = self.head;
            else:
                self.head = self.tail = None;

    def delete_end(self):
        if (self.head == None):
            return
        else:
            if (self.head != self.tail):
                current = self.head
                while (current.next != self.tail):
                    current = current.next
                self.tail = current
                self.tail.next = self.head
            else:
                self.head = self.tail = None

    def traverse(self):
        temp = self.head
        if self.head is not None:
            while (True):
                print("%d" % (temp.data), end='  ')
                temp = temp.next
                if (temp == self.head):
                    break


List = my_circular_list()
List.add_node(34)
List.add_node(45)
List.add_node(55)
List.add_node(65)
List.add_node(86)
List.add_node(76)
print("Created linked list:")
List.traverse()
print()
List.insert_at_end(53)
List.insert_at_end(21)
List.insert_at_beginning(78)
List.insert_at_beginning(38)
print("\nUpdated list: Insertion of 53 and 21 at the end, and 78 and 38 at the beginning:")
List.traverse()
print()
List.delete_start()
List.delete_end()
print("\nLinked List after deletion at the start and end :")
List.traverse()




