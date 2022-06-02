class node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def left_height(node):
    ht = 0
    while (node):
        ht += 1
        node = node.left
    return ht

def right_height(node):
    ht = 0
    while (node):
        ht += 1
        node = node.right
    return ht

def TotalNodes(root):
    if (root == None):
        return 0
    lh = left_height(root)
    rh = right_height(root)
    if (lh == rh):
        return (1 << lh) - 2
    return TotalNodes(root.left) + TotalNodes(root.right)

root = node(10)
root.left = node(5)
root.right = node(20)
root.left.left = node(2)
root.right.right = node(30)
root.right.right.left = node(25)
print("The total number of Node is", TotalNodes(root))
