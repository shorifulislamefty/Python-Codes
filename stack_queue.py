# Stack version 1
class Stack:
    def __init__(self):
        self.values=[]
    def push(self,data):
        self.values=[data]+self.values
    def pop(self):
        return self.values.pop(0)
    def traversal(self):
        for val in self.values:
            print(val,end=" ")    

s=Stack()
n=int(input())
for i in range(n):
    data=int(input(f"Enter {i+1} number data:"))
    s.push(data)
s.traversal() 

# Queue version 1
class Queue:
    def __init__(self):
        self.values=[]
    def enqueue(self,data):
        self.values.append(data)
    def dequeue(self):
        # front=self.values[0]
        # self.values=self.values[1:]
        front=self.values.pop(0)
        return front
    def traversal(self):
        for val in self.values:
            print(val,end=" ")    

q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.traversal()

# Stack version 2
stack = []
n=int(input())
for i in range(n):
    data=int(input(f"Enter {i+1} number data:"))
    stack.append(data)
while stack !=[]:
    top=stack.pop()
    print(top,end=" ") 

# Queue version 2
queue = []
n=int(input())
for i in range(n):
    data=int(input(f"Enter {i+1} number data:"))
    queue.append(data)
while queue !=[]:
    top=queue.pop(0)
    print(top,end=" ")
    