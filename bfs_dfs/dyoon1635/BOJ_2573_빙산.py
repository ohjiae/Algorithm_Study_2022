import copy
import sys
sys.setrecursionlimit(10000)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
iceberg = []
for i in range(n):
    iceberg.append(list(map(int, input().split())))
visited = []

def out_of_bound(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return True
    return False

def melt():
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                cnt = 0
                for k in range(4):
                    if not out_of_bound(i + dx[k], j + dy[k]) and \
                            iceberg[i+dx[k]][j+dy[k]] == 0:
                        cnt += 1
                iceberg[i][j] -= cnt
                if iceberg[i][j] == 0: iceberg[i][j] = -1
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] < 0:
                iceberg[i][j] = 0


def bfs(x, y):
    global visited
    if out_of_bound(x, y): return None
    if visited[x][y] or iceberg[x][y] == 0: return None
    visited[x][y] = True
    for i in range(4):
        bfs(x + dx[i], y + dy[i])

def solve():
    res = 0
    global visited
    while True:
        cnt = 0
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not visited[i][j] and iceberg[i][j] > 0:
                    bfs(i, j)
                    cnt += 1
        if cnt > 1:
            print(res)
            break
        elif cnt == 0:
            print(0)
            break
        melt()
        res += 1

if __name__ == "__main__":
    solve()