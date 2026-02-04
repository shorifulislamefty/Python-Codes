# Adj_matrix
n,e=map(int,input().split())
adj_mat=[[0 for _ in range(n)] for _ in range(n)]
for _  in range(e):
    a,b=map(int,input().split())
    adj_mat[a][b]=1
    adj_mat[b][a]=1
    
for i in range(n):
    adj_mat[i][i]=1

for i in range(n):
    for j in range(n):
        print(adj_mat[i][j],end=" ")
    print() 


# Adjacency list 
n,e=map(int,input().split())
adj_list=[[] for _ in range(n)]
for i in range(e):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
for i in range(n):
    print(f"{i}-->",end=" ")
    for val in adj_list[i]:
        print(val,end=",") 
    print()  

# Edge List:
n,e=map(int,input().split())
edge_list=[]
for _ in range(n):
    a,b=map(int,input().split())
    edge_list.append((a,b))

print("Output:-")
for p,q in edge_list:
    print(p,q)
#Graph Traversal BFS:
def bfs(adj_list,src,n):
    vis=[False]*105
    queue=[]
    queue.append(src)
    vis[src]=True
    while queue:
        par=queue.pop(0)
        print(par,end=" ")
        for child in adj_list[src]:
            if vis[child]==False:
                queue.append(child) 
                vis[child]=True

n,e=map( int,input().split())
adj_list=[[] for _ in range(n)]
for _ in range(e):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
bfs(adj_list,0,n) 

#Graph traversal DFS:
def dfs(adj_list,src,vis):
    print(src,end=" ")
    vis[src]=True
    for child in adj_list[src]:
        if vis[child]==False:
            dfs(adj_list,child,vis)

vis=[False]*105
n,e=map( int,input().split())
adj_list=[[] for _ in range(n)]
for _ in range(e):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
dfs(adj_list,0,vis) 

#2D arry by List:
n, m = map(int, input().split())
grid = [['' for _ in range(m)] for _ in range(n)]

for i in range(n):
    grid[i] = input().split()

print("output-->:")
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()

#Grid DFS:
n, m = map(int, input().split())
grid = [['' for _ in range(m)] for _ in range(n)]
for i in range(n):
    grid[i] = input().split()
move=[(-1,0),(1,0),(0,1),(0,-1)]
vis=[[False for _ in range(m)] for _ in range(n)]

def valid(i,j):
    if i>0 or i>=n or j>0 or j>=m:
        return False
    return True     

def dfs(si,sj):
    print(si,sj)
    vis[si][sj]=True
    for mx,my in move:
        ci=si+mx
        cj=sj+my
        if valid(ci,cj) and not vis[ci][cj]:
            dfs(ci,cj)

si,sj=map(int,input().split())
dfs(si,sj) 

# Grid BFS
n, m = map(int, input().split())
grid = [['' for _ in range(m)] for _ in range(n)]
for i in range(n):
    grid[i] = input().split()
move=[(-1,0),(1,0),(0,1),(0,-1)]
vis=[[False for _ in range(m)] for _ in range(n)]

def valid(i,j):
    if i<0 or i>=n or j<0 or j>=m:
        return False
    return True     

def bfs(si,sj):
    queue=[]
    queue.append((si,sj))
    vis[si][sj]=True
    while queue:
        pi,pj=queue.pop(0)
        print(pi,pj)
        for i,j in move:
            ci=pi+i 
            cj=pj+j
            if valid(ci,cj)  and not vis[ci][cj]:
                queue.append((ci,cj))
                vis[ci][cj]


si,sj=map(int,input().split())
bfs(si,sj) 

#Cycle detected BFS:
vis=[False]*105
parent=[-1]*105
def bfs(adj_list,src,n):
    cycle=False
    queue=[]
    queue.append(src)
    vis[src]=True
    while queue:
        par=queue.pop(0)
        print(par,end=" ")
        for child in adj_list[par]:
            if vis[child] and parent[par] !=child:
                cycle=True
            if vis[child]==False:
                queue.append(child) 
                vis[child]=True
                parent[child]=par
    return cycle         

n,e=map( int,input().split())
adj_list=[[] for _ in range(n)]
for _ in range(e):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)    
if bfs(adj_list,0,n):
    print("cycle detected")
else:
    print("cycle not detected")

#Cycle detected in DFS:
vis=[False]*105
parent=[-1]*105
n,e=map( int,input().split())
adj_list=[[] for _ in range(n)]
def dfs(src,n):
    print(src,end=" ")
    vis[src]=True
    for child in adj_list[src]:
        if vis[child] and parent[src] !=child:
            return True
        if vis[child]==False:
            parent[child]=src
            dfs(child,n)
            
for _ in range(e):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)    
cycle=dfs(0,n)
if cycle ==True:
    print("cycle detected")
else:
    print("cycle not detected") 

#Adj_list for Dijkstra
n,e=map(int,input().split())
adj_list=[[] for _ in range(n)]
for _ in range(e):
    a,b,c=map(int,input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))
for i in range(n):
    print(f"{i}-->")
    for x,y in adj_list[i]:
        print(x,y,end=",")
    print()

# Priority Queue
import heapq
queue=[7,4,5,55]
heapq.heapify(queue)
heapq.heappush(queue,50)
heapq.heappush(queue,30)
heapq.heappush(queue,60)
heapq.heappush(queue,10)
heapq.heappush(queue,0)
heapq.heappush(queue,-11)
print("after the value apand\n")
while queue:
    print(heapq.heappop(queue),end=" ")

# Dijkstra Optimized way:
import math
import heapq
n,e=map(int,input().split())
INF=math.inf
dis=[INF]*n
adj_list=[[] for _ in range(n)]
for _ in range(e):
    a,b,c=map(int,input().split())
    adj_list[a].append((b,c))
    adj_list[b].append((a,c))
def dijkstra(src):
    queue=[]
    heapq.heappush(queue,(0,src)) 
    dis[src]=0
    while queue:
        par_Node,par_dis=queue.pop(0)
        for child in adj_list[par_Node]:
            child_Node,child_dis=child
            if par_dis+child_dis<dis[child_Node]:
                heapq.heappush(queue,(par_dis+child_dis,child_Node))
                dis[child_Node]=par_dis+child_dis

dijkstra(0)
for i in range(n):
    print(dis[i],end=" ") 

# Bellman ford :
import math 
INF=math.inf
list=[]
n,e=map(int,input().split())
dis=[INF]*n
dis[0]=0
for _ in range(e):
    a,b,c=map(int,input().split())
    list.append((a,b,c))
def bellman_ford():
    for _ in range(n-1):
        for tpl in list:
            a,b,c=tpl
            if dis[a] !=INF and dis[a]+c<dis[b]:
                dis[b]=dis[a]+c


bellman_ford()
for i in range(n):
    print(f"{i}-->{dis[i]}")

#Negative cycle detected
import math 
INF=math.inf
list=[]
n,e=map(int,input().split())
dis=[INF]*n
dis[0]=0
for _ in range(e):
    a,b,c=map(int,input().split())
    list.append((a,b,c))
def bellman_ford():
    cycle=False
    for _ in range(n-1):
        for tpl in list:
            a,b,c=tpl
            if dis[a] !=INF and dis[a]+c<dis[b]:
                dis[b]=dis[a]+c     
    for tpl in list:
        a,b,c=tpl
        if dis[a] !=INF and dis[a]+c<dis[b]:
           cycle=True
           break
    return cycle                  


if bellman_ford():
    print("Negative cycle detected")
else:
      print("Not Negative cycle detected") 

#Floyed warshall
import math
INF=math.inf
n,e=map(int,input().split())
adj_mat=[[INF for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            adj_mat[i][j]=0
for _ in range(e):
    a,b,c=map(int,input().split())
    adj_mat[a][b]=c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj_mat[i][k]!=INF and adj_mat[k][j]!=INF and adj_mat[i][k]+adj_mat[k][j] < adj_mat[i][j]:
                adj_mat[i][j]=adj_mat[i][k]+adj_mat[k][j]
for i in range(n):
    for j in range(n):
        print(adj_mat[i][j],end=" ")
    print()     

#Floyed warshall-Negative weighted cycle detected
import math
INF=math.inf
n,e=map(int,input().split())
adj_mat=[[INF for _ in range(n)]for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            adj_mat[i][j]=0
for _ in range(e):
    a,b,c=map(int,input().split())
    adj_mat[a][b]=c
for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj_mat[i][k]!=INF and adj_mat[k][j]!=INF and adj_mat[i][k]+adj_mat[k][j] < adj_mat[i][j]:
                adj_mat[i][j]=adj_mat[i][k]+adj_mat[k][j]
for i in range(n):
    if adj_mat[i][i]<0:
        print('Negative weighted cycle detected.\n')
    else:
        for i in range(n):
            for j in range(n):
                print(adj_mat[i][j],end=" ")
        print() 

#Find leader using loop
leader=[-1]*10
leader[0]=1
leader[1]=-1
leader[2]=1
leader[3]=1
leader[4]=5
leader[5]=3
def find_leader(node):
    while leader[node]!=-1:  
        node=leader[node]
    return node
print(find_leader(5))

#Find leader using recurtion
leader=[-1]*10
leader[0]=1
leader[1]=-1
leader[2]=1
leader[3]=1
leader[4]=5
leader[5]=3
def find_leader(node):  
    if leader[node]==-1:
        return 
    leader[node]=find_leader     
    return find_leader(leader[node])    
print(find_leader(5)) 

#Find leader using recurtion optimizing
leader=[-1]*10
leader[0]=1
leader[1]=-1
leader[2]=1
leader[3]=1
leader[4]=5
leader[5]=3
def find_leader(node):  
    if leader[node]==-1:
        return node
    ldr= find_leader(leader[node]) 
    leader[node]=ldr
    return ldr

print(find_leader(5))

#DSU_Find_union operation:
leader=[-1]*105
group_size=[1]*105
def find_leader(node):  
    if leader[node]==-1:
        return node
    leader[node]= find_leader(leader[node]) 
    return leader[node]
def dsu_union(node1,node2):
    leader1=find_leader(node1)
    leader2=find_leader(node2)
    if group_size[leader1]>=group_size[leader2]:
        leader[leader2]=leader1
        group_size[leader1]+=group_size[leader2]
    else:
        leader[leader1]=leader2
        group_size[leader2]+=group_size[leader1]

dsu_union(1,2)
dsu_union(2,0)
dsu_union(3,1)
for i in range(6):
    print(f"{i}-->",leader[i])

