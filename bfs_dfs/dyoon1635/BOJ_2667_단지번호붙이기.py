n = int(input())
visited = [[False] * n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
board = []
cnt = 0

def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for i in range(4):
        if x + dx[i] >= 0 and x + dx[i] < n and \
            y + dy[i] >= 0 and y + dy[i] < n and \
            not visited[x + dx[i]][y + dy[i]] and \
                board[x + dx[i]][y + dy[i]] == 1:
            dfs(x + dx[i], y + dy[i])

if __name__ == "__main__":
    for _ in range(n):
        board.append(list(map(int, input())))

    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 and not visited[i][j]:
                cnt = 0
                dfs(i, j)
                res.append(cnt)
    res.sort()
    print(len(res))
    for i in res: print(i)