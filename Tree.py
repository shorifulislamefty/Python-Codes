#DFS
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.roat=None
    def preOder_traversal(self,roat):
        if roat ==None:
            return
        print(roat.val,end=" ") 
        self.preOder_traversal(roat.left)
        self.preOder_traversal(roat.right)

    def ineOder_traversal(self,roat):
        if roat ==None:
            return 
        self.ineOder_traversal(roat.left)
        print(roat.val,end=" ")
        self.ineOder_traversal(roat.right) 

    def postOder_traversal(self,roat):
        if roat ==None:
            return
        self.postOder_traversal(roat.left)
        self.postOder_traversal(roat.right)
        print(roat.val,end=" ")       

n1=Node(10)
n2=Node(20) 
n3=Node(30) 
n4=Node(40) 
tree=Tree()
tree.roat=n1
tree.roat.left=n2
tree.roat.right=n3
n2.left=n4
tree.preOder_traversal(tree.roat)
print(end="\n")  
tree.ineOder_traversal(tree.roat)
print(end="\n") 
tree.postOder_traversal(tree.roat)    

#BFS
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def level_traversal(self,root):
        if root==None:
            return
        queue=[]
        queue.append(root)
        while queue !=[]:
            front=queue.pop(0)
            print(front.val,end=' ')
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)

n1=Node(10)
n2=Node(20)
n3=Node(30)
n4=Node(40)
n5=Node(50)
tree=Tree()
tree.root=n1
tree.root.left=n2
tree.root.right=n3
n2.left=n4
tree.level_traversal(n1)

#Input Binary Tree:
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def input_tree(self):
        val=int(input("Enter the root value:"))
        if val==-1:
            return None
        root=Node(val)
        queue=[]
        queue.append(root)
        while queue !=[]:
            p=queue.pop(0)
            l,r=map(int,input(f"Enter the child l,r of {p.val}:").split()) 
            if l==-1:
                p.left=None
            else:
                p.left=Node(l)
                queue.append(p.left)
            if r==-1:
                p.right=None
            else:
                p.right=Node(r)
                queue.append(p.right)
        return root

    def level_traversal(self,root):
        if root==None:
            return
        queue=[]
        queue.append(root)
        while queue !=[]:
            p=queue.pop(0)
            print(p.val,end=" ")
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)


tree=Tree()
tree.root=tree.input_tree()
tree.level_traversal(tree.root)    
# Insert the value in BST:
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
class Tree:
    def __init__(self):
        self.root=None
    def input_tree(self):
        val=int(input("Enter the value:"))
        root=Node(val)
        queue=[]
        queue.append(root)
        while queue !=[]:
            p=queue.pop(0)
            l,r=map(int,input(f"Enter the value l & r of {p.val}:").split())
            if l==-1:
                p.left=None
            else:
                p.left=Node(l)
                queue.append(p.left)
            if r ==-1:
                p.right=None
            else:
                p.right=Node(r)
                queue.append(p.right)
        return root

    def insert_tree(self,root,value):
        if root==None:
            root=Node(value)
        if root.val > value:
           if root.left==None:
            root.left=Node(root.left)
           else:
            self.insert_tree(root.left,value) 
        else: 
            if root.right==None:
                root.right=Node(value)
            else:
                self.insert_tree(root.right,value)

    def level_traversal(self,root): 
        if root ==None:
            return
        queue=[]
        queue.append(root)
        while queue !=[]:
            p=queue.pop(0)
            print(p.val,end=" ")
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)                               

tree=Tree()
tree.root=tree.input_tree()
insert_value=int(input("Enter the search value:"))
tree.insert_tree(tree.root,insert_value)
tree.level_traversal(tree.root)
