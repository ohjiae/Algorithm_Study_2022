n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
result = []
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global cnt
    cnt+=1
    graph[x][y] = 0

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if graph[nx][ny] == 1:
            dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt=0
            dfs(i, j)
            result.append(cnt)

print(len(result))
print(*sorted(result), sep='\n')