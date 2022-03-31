import sys, copy
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

bfs = deque()
#visited = [[1] * m for _ in range(n)]
bfs.append([(0, 0), False, 1, -999])
while True:
    if not bfs: break
    cur, broken, cnt, ex = bfs.popleft()
    for i in range(4):
        if (ex + 2)%4 == i: continue
        nx = cur[0] + dx[i]
        ny = cur[1] + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if nx == n - 1 and ny == m - 1:
                print(cnt + 1)
                #for i in range(n): print(visited[i])
                exit(0)

            if board[nx][ny] == 0:
                bfs.append([(nx, ny), broken, cnt + 1, i])
            elif board[nx][ny] == 1 and not broken:
                bfs.append([(nx, ny), True, cnt + 1, i])
print(-1)