from collections import deque
import sys
input = sys.stdin.readline
INF = sys.maxsize

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m= map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
distance = [[[INF]*2 for _ in range(m)] for _ in range(n)]

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y, 0))
    distance[start_x][start_y][0]=1

    while queue:
        x, y, s = queue.popleft()

        if x == n-1 and y == m-1:
            return min(distance[n-1][m-1])

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 0 and distance[nx][ny][s] == INF:
                distance[nx][ny][s] = distance[x][y][s]+1
                queue.append((nx, ny, s))
            elif graph[nx][ny] == 1 and s < 1 and distance[nx][ny][s+1] == INF:
                distance[nx][ny][s+1]=distance[x][y][s]+1
                queue.append((nx, ny, s+1))
    return -1
  
print(bfs(0, 0))