from sys import stdin
input = stdin.readline
N = int(input())
graph = [list(map(int,list(input().rstrip()))) for _ in range(N)]
vis = [[False for _ in range(N)] for _ in range(N)]
#print(*vis, sep='\n')
mx = [1,0,-1,0]
my = [0,1,0,-1]
res = []
cnt = 0

def dfs(row,col,c):
    cnt = c
    if 0 <= row < N and 0 < col < N and not vis[row][col]:
        vis[row][col]=True
        if graph[row][col]:
            cnt += 1
            for i in range(4):
                dfs(row+mx[i],col+my[i],cnt)

for r in range(N):
    for c in range(N):
        if graph[r][c]:
            dfs(r,c,cnt)
            if cnt > 0:
                res.append(cnt)
                cnt = 0
print(res)
