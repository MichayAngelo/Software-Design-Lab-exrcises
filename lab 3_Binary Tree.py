class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def BinaryTree(val):
    if (root.data == None):
        print(val, " Inserted as root")
        root.data = val
    else:
        p = root
        n = Node()
        n.data = val
        while (1):
            if (val < p.data):
                if (p.left == None):
                    print(val, "Inserted on left of", p.data)
                    p.left = n
                    break
                else:
                    p = p.left
            else:
                if (p.right == None):
                    print(val, "Inserted on right of", p.data)
                    p.right = n
                    break
                else:
                    p = p.right

root = Node()
BinaryTree(10)
BinaryTree(5)
BinaryTree(20)
BinaryTree(30)
BinaryTree(25)
BinaryTree(2)