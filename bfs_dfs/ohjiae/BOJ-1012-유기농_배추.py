import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
def dfs(g,y,x):
    g[y][x] = 0
    for i in [(1,0),(0,1),(0,-1),(-1,0)]:
        if 0<= x+i[1]<M and 0<=y+i[0]<N and g[y+i[0]][x+i[1]] == 1:
            dfs(g,y+i[0],x+i[1])
T = int(input())
for i in range(T):
    cnt = 0
    M,N,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,input().split())
        graph[Y][X] = 1
    for row in range(N):
        for col in range(M):
            if graph[row][col] == 1:
                cnt += 1
                dfs(graph,row,col)
    print(cnt)