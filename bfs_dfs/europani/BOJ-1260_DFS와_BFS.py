from collections import deque

v, e, s = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a].sort()
    graph[b].append(a)
    graph[b].sort()

def dfs(v):
    print(v, end=' ')
    visited[v]=True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    visited = [False] * (v+1)

    queue = deque([start])
    visited[start]=True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

dfs(s)
print()
bfs(s)