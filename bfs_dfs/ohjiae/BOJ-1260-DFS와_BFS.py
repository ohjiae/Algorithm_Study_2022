import sys
from collections import deque
N, M, V = map(int,input().split())
# input = sys.stdin.readline

graph = {}
for _ in range(M):
    p, c = map(int,input().split())
    if p in graph: graph[p].append(c)
    else: graph[p] = [c]

dis = [False] * (N + 1)
def dfs(graph,V):
    dis[V] = True
    print(V,end=' ')
    if V in graph:
        for i in graph[V]:
            if not dis[i]:
                dfs(graph,i)

bis = [False] * (N + 1)
q=deque(V)
def bfs(graph,V):
    while q:
        node = q.popleft()
        bis[node] = True
        print(node, end=' ')
        if node in graph and len(graph[node])!=0:
            for i in graph[node]:
                if not bis[i]:
                    q.append(i)     

dfs(graph,V)
bfs(graph,V)
