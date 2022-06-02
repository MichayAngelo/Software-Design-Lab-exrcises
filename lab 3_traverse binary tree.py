class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def PostPreInOrderInOneFlowRecursive(root, pre, post, In):
    if (root == None):
        return
    pre.append(root.data)
    PostPreInOrderInOneFlowRecursive(root.left, pre, post, In)
    In.append(root.data)
    PostPreInOrderInOneFlowRecursive(root.right, pre, post, In)
    post.append(root.data)


root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(2)
root.right.right = Node(30)
root.right.right.left = Node(25)
pre, post, In = [], [], []
PostPreInOrderInOneFlowRecursive(root, pre, post, In)
print("Pre Order : ", end=" ")
for i in pre:
    print(i, end=", ")
print()
print("Post Order : ", end=" ")
for i in post:
    print(i, end=", ")
print()
print("In Order : ", end=" ")
for i in In:
    print(i, end=", ")

