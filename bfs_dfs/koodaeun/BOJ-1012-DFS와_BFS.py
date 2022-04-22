#BOJ-1012-DFS와_BFS
import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())    
graph = [[] for i in range(n+1)]

for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)   

def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')
    graph[start].sort()     
    for node in graph[start]:
        if not visited[node]:
            dfs(graph, node, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        graph[now].sort()       
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

visited = [False] * (n+1)
dfs(graph, start, visited)
visited = [False] * (n+1)
print()
bfs(graph, start, visited)