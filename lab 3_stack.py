stack = []
def top(stack):
    if stack != []:
        print(stack[-1] + " is topmost element")
    else:
        print("Stack Empty!!!")
def size(stack):
        print("Size of stack is " + str(len(stack)))
def empty(stack):
    if stack == []:
        print("The stack is empty.")
    else:
        print("The stack is", stack)

stack.append('a')
stack.append('b')
stack.append('c')
size(stack)
print(stack)
print()
top(stack)
print()
print(stack.pop() + " is popped")
print(stack)
print()
empty(stack)
print(stack.pop() + " is popped")
print(stack.pop() + " is popped")
empty(stack)


