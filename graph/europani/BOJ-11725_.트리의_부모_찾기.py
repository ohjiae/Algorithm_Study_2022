from collections import deque

n = int(input())
graph = [list() for _ in range(n+1)]
parent = [-1] * (n+1)

def bfs(start):
    queue = deque([start])
    parent[start]=start

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            if parent[i]==-1:
                parent[i]=now
                queue.append(i)
        
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(1)

for i in range(2, n+1):
    print(parent[i])