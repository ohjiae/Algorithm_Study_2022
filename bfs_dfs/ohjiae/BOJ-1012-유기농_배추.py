def dfs(g,y,x):
    g[y][x] = 0
    for i in [(-1,0),(0,1),(0,-1),(1,0)]:
        if 0<= x+i[0] <M and 0<= y+i[1] <N and g[y+i[0]][x+i[1]] == 1:
            dfs(g,y+i[0],[x+i[1]])

T = int(input())
for i in range(T):
    cnt = 0
    M,N,K = map(int,input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for where in range(K):
        X,Y = map(int,input().split())
        graph[Y][X] = 1
    print(*graph,sep='\n')
    for row in range(N):
        for col in range(M):
            if graph[col][row] == 1:
                cnt += 1
                print(f'T={i},col={col},row={row},cnt={cnt},gcr={graph[row][col]}')
                dfs(graph,row,col)


