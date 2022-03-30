import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())    #정점개수/간선개수/시작정점번호
graph = [[] for i in range(n+1)]


for i in range(m):
    n1, n2 = map(int, sys.stdin.readline().split())
    graph[n1].append(n2)
    graph[n2].append(n1)    #인접리스트로 구현

#print(graph)    # [[], [2, 3, 4], [1, 3], [1, 2, 4], [1, 3]]


def dfs(graph, start, visited):
    visited[start] = True
    print(start, end=' ')

    graph[start].sort()     #**문제조건; 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은것을 먼저 방문
    for node in graph[start]:

        if not visited[node]:
            dfs(graph, node, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        graph[now].sort()       #**문제조건; 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은것을 먼저 방문
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (n+1)

dfs(graph, start, visited)
visited = [False] * (n+1)
print()
bfs(graph, start, visited)