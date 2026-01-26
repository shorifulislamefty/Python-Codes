class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def Front_traversal(self):
        if self.head==None:
            print("the doubly linked list")
        else:
            temp=self.head
            while temp !=None:
                print(temp.data,end=" ")
                temp=temp.next

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
dll=Dll()
dll.head=n1
dll.tail=n4
dll.head.next=n2
n2.prev=dll.head
n2.next=n3
n3.prev=n2
n3.next=dll.tail
dll.tail.prev=n3
dll.Front_traversal()
