from collections import deque

n, m, start = map(int, input().split())
linked = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    linked[x][y] = 1
    linked[y][x] = 1


def dfs():
    dq = deque()
    dq.append(start)
    visited = [False] * (n + 1)
    while dq:
        cur = dq.pop()
        if visited[cur]: continue
        visited[cur] = True
        print(cur, end=' ')
        for i in reversed(range(1, n + 1)):
            if linked[cur][i] and not visited[i]:
                dq.append(i)
    print('')

def bfs():
    dq = deque()
    dq.append(start)
    visited = [False] * (n + 1)
    while dq:
        cur = dq.popleft()
        if visited[cur]: continue
        visited[cur] = True
        print(cur, end=' ')
        for i in range(1, n+1):
            if linked[cur][i] and not visited[i]:
                dq.append(i)
dfs()
bfs()