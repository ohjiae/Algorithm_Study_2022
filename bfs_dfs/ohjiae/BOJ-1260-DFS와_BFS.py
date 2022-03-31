from collections import deque
import sys
input = sys.stdin.readline
N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
vis = [False for _ in range(N+1)]
res = []
for i in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
for j in graph:
    if len(j)>1:
        j.sort()
stack = deque()
def dfs(V):
    res.append(V)
    vis[V] = True
    stack.append(V)
    node = stack.pop()
    for i in graph[node]:
        if not vis[i]:
            dfs(i)
dfs(V)
print(*res)
res = []
def bfs():
    vis = [False for _ in range(N+1)]
    q = deque([V])
    vis[V] = True
    while q:
        node = q.popleft()
        res.append(node)
        for n in graph[node]:
            if not vis[n]:
                q.append(n)
                vis[n] = True
bfs()
print(*res)