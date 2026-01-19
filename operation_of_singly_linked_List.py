class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None 
    def sum(self):
        sum=0
        if self.head == None:
            print("The linked list is empty")
        else:
            temp=self.head
            while temp !=None:
                sum+=temp.data
                temp=temp.next
            print(sum)
    def add_node_at_head(self,h):
        if self.head == None:
            print("The linked list is empty")
        else:
            new_node=Node(h)   
            new_node.next=self.head
            self.head=new_node 

    def add_node_at_tail(self,h):
        new_node=Node(h)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next !=None:
                temp=temp.next
            temp.next=new_node 

    def add_node_at_any_position(self,h,r):
        new_node=Node(h)
        if self.head==None:
            print("the linked list is empty")
        else:
            temp=self.head
            for _ in range(r-1):
                temp=temp.next
            new_node.next=temp.next.next
            temp.next=new_node

    def delete_node_at_head(self):
        if self.head==None:
            print("the linked is empty")
            return
        else:
            # self.head=self.head.next  
            deleteNode=self.head
            self.head=self.head.next
            del deleteNode

    def delete_node_at_any_position(self,i):
        if self.head==None:
            print("The linked list is empty")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            for _ in range(i-1):
                temp=temp.next
            temp.next=temp.next.next    

    def delete_at_tail(self):
        if self.head==None:
            print("the linked list is emmpty")
        elif self.head.next==None:
            self.head=None
        else:
            temp=self.head
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None     

    def traversal(self):
        if self.head==None:
            print("the link list is empty")
        else:
            temp=self.head
            while temp !=None:
                print(temp.data,end=" ")
                temp=temp.next

n1=Node(2)
n2=Node(40)
n3=Node(23)
n4=Node(20)
sll=Sll()
sll.head=n1
n1.next=n2
n2.next=n3
n3.next=n4
sll.add_node_at_any_position(203,2)
sll.add_node_at_tail(90)
sll.add_node_at_head(11)
sll.delete_node_at_head()
sll.delete_at_tail()
sll.delete_node_at_any_position(1)
sll.sum()
sll.traversal()

