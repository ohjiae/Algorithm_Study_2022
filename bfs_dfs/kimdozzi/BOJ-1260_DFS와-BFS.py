import sys
from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        temp = queue.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m) :
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1) :
    graph[i].sort()

dfs(graph,v,visited)
print(end='\n')
visited = [False] * (n+1)
bfs(graph,v,visited)




