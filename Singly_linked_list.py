class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("signly linklist is empty")
        else:
            temp=self.head
            while temp is not None:
                print(temp.data,end=" ")
                temp=temp.next

n1=Node(3)
n2=Node(5)
n3=Node(6)
n4=Node(10)
sll=Sll()
sll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
sll.traversal()