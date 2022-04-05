def dfs(g,x,y):
    g[x][y] = 0
    for i in [(-1,0),(0,1),(0,-1),(1,0)]:
        if 0<= x+i[0] <N and 0<= y+i[1] <M and g[x+i[0]][y+i[1]] == 1:
            dfs(g,x+i[0],y+i[1])

T = int(input())
cnt = 0
for i in range(T):
    M,N,K = map(int,input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for where in range(K):
        X,Y = map(int,input().split())
        graph[X][Y] = 1
    for col in range(M):
        for row in range(N):
            if graph[col][row] == 1:
                cnt += 1
                print(f'T={t},col={col},row={row},cnt={cnt},gcr={graph[col][row]}')
                dfs(graph,col,row)


