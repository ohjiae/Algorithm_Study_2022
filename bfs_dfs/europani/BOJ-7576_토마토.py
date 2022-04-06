import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

def find_max():
    max_day = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j]==0:
                return -1
            if graph[i][j] > max_day:
                max_day = graph[i][j]

    return max_day-1

def bfs():
    queue = deque()

    # 초기화
    for i in range(m):
        for j in range(n):
            if graph[i][j]==1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
    
            if graph[nx][ny] == 0:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx, ny))

bfs()
print(find_max())