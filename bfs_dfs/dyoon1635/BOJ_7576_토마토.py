from collections import deque

m, n = map(int, input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
box = []
tomato = deque()
for i in range(n):
    box.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            tomato.append([(i, j), 0])

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    return False

def is_ripen():
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                return False
    return True

cnt = 0
while tomato:
    (cx, cy), cnt = tomato.popleft()
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if not out_of_bound(nx, ny):
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                tomato.append([(nx, ny), cnt + 1])

if is_ripen(): print(cnt)
else: print(-1)