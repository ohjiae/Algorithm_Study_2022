from collections import deque

n = int(input())
board = [] * n
for i in range(n):
    board.append(list(map(int, input().split())))

shark_size = 2
cnt = 0 # 상어가 먹은 먹이 수 check
sx = -1 # shark_x
sy = -1 # shark_y
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            sx, sy = i, j

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def valid(x, y):
    # out of bound
    if x < 0 or x >= n or y < 0 or y >= n: return False
    # 상어보다 size 큰 물고기는 못 지나감
    if board[x][y] > shark_size: return False
    return True

def eat(x, y): # (x, y)에 위치한 물고기를 먹음
    global cnt, shark_size
    board[x][y] = 0
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0

def bfs():
    q = deque()
    q.append([sx, sy, 0]) # [좌표, 거리(시간)]
    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True

    while q:
        cur = q.popleft()
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]

            if valid(x, y) and not visited[x][y]:
                visited[x][y] = True
                if 0 < board[x][y] < shark_size:
                    eat(x, y)
                    #####################
                    print(x, y, cur[2]+1)
                    #####################
                    return [x, y, cur[2] + 1]
                q.append([x, y, cur[2] + 1])
    return None

def solve():
    global sx, sy
    res = 0
    while True:
        cur = bfs()
        if cur is None:
            print(res)
            return None
        res += cur[2]
        sx, sy = cur[0], cur[1]

if __name__ == "__main__":
    solve()