import sys
sys.setrecursionlimit(10000)

t = int(input().strip())
visited = []
field = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def bfs(x, y, n, m):
    if x < 0 or x >= n or \
        y < 0 or y >= m:
        return None
    if visited[x][y] == True or\
            field[x][y] == 0: return None
    visited[x][y] = True
    for i in range(4):
        bfs(x + dx[i], y + dy[i], n, m)

def solve():
    global visited, field
    m, n, k = map(int, input().split())
    field = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1 and visited[i][j] == False:
                cnt += 1
                bfs(i, j, n ,m)
    return cnt
for _ in range(t):
    print(solve())
