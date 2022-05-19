from collections import deque

n=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

vis=[-1]*(n+1)

def bfs(a):
    deq=deque()
    deq.append(a)
    vis[a]=0
    while deq:
        node=deq.popleft()
        for i in graph[node]:
            if vis[i] == -1:
                deq.append(i)
                vis[i]=node

bfs(1)

for i in range(2,n+1):
    print(vis[i])