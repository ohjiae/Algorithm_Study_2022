# BOJ-7576-토마토

import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

toma_box = []
queue = deque([])

# 토마토 받아서 넣는 이차원 리스트
# queue에 처음에 받은 토마토의 위치 좌표를 append시킨다
for i in range(n):
    toma_box.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):      # 익은 토마토를 큐에 저장
        if toma_box[i][j] == 1:
            queue.append([i, j])

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 토마토 익히기
def bfs():

    while queue:
        x, y = queue.popleft()  # 처음 토마토 좌표 x, y에 꺼내고

        for i in range(4):      # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
            nx = dx[i] + x
            ny = dy[i] + y

            # 해당 좌표가 좌표크기를 넘어가서는 x, 또한 그 좌표에 토마토가 익지 않은채로 있어야함 == 0
            if 0 <= nx < n and 0 <= ny < m and toma_box[nx][ny] == 0:
                toma_box[nx][ny] = toma_box[x][y] + 1       # 익히고 1을 더해주면서 횟수를 세어준다.
                queue.append([nx, ny])                      # 여기서 나온 제일 큰 값이 정답이 됨

bfs()
result = 0

# 최단거리를 toma_box에 다 표시한 뒤, 0이 존재하면 -1을 출력한다.
for i in toma_box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)                 #break로 하면 80%에서 틀림
    result = max(result, max(i))    #0이 존재하지 않으면 최대값을 출력해준다.
print(result-1)                     #처음을 1로 시작했으므로 -1을 해준다.