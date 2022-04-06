# 토마토

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

toma_box = []
queue = deque([])

for i in range(n):
    toma_box.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):      
        if toma_box[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():

    while queue:
        x, y = queue.popleft()

        for i in range(4):    
            nx = dx[i] + x
            ny = dy[i] + y

            
            if 0 <= nx < n and 0 <= ny < m and toma_box[nx][ny] == 0:
                toma_box[nx][ny] = toma_box[x][y] + 1    
                queue.append([nx, ny])      

bfs()
result = 0

for i in toma_box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)   
    result = max(result, max(i))    
print(result-1)    