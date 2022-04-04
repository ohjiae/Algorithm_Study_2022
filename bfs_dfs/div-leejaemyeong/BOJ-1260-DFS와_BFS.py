from collections import deque

n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    
for i in range(n+1):
    graph[i].sort()
    
visit_dfs=[False]*(n+1)
visit_bfs=[False]*(n+1)
dfs=[]
bfs=[]

def DFS(v):
    dfs.append(v)
    visit_dfs[v]=True
    for i in graph[v]:
        if not visit_dfs[i]:
            DFS(i)

def BFS(v):
    deq=deque()
    deq.append(v)
    visit_bfs[v]=True
    while deq:
        now=deq.popleft()
        bfs.append(now)
        for i in graph[now]:
            if not visit_bfs[i]:
                deq.append(i)
                visit_bfs[i]=True
                
DFS(v)
BFS(v)
print(' '.join(str(i)for i in dfs))
print(' '.join(str(i)for i in bfs))
