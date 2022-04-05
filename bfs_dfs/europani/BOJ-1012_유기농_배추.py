import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, graph):
    graph[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= a or ny >= b:
            continue

        if graph[nx][ny]==1:
            dfs(nx, ny, graph)

t = int(input())

for _ in range(t):
    result = 0

    a, b, n = map(int, input().split())
    graph = [[0] * b for _ in range(a)]
    
    for _ in range(n):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(a):
        for j in range(b):
            if graph[i][j] == 1:
                result+=1
                dfs(i, j, graph)
    print(result)