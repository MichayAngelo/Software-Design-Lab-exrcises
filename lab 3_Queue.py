def enqueue(data):
   queue.insert(0, data)

def dequeue():
   if len(queue) > 0:
      return queue.pop()
   return ("Queue Empty!")

def display():
   print("Elements on queue are:")
   for i in range(len(queue)):
      print(queue[i], end=" ")


queue=[]
enqueue(5)
enqueue(6)
enqueue(9)
enqueue(5)
enqueue(3)
print("Queue:", queue)
print("Popped Element is: "+str(dequeue()))
display()
