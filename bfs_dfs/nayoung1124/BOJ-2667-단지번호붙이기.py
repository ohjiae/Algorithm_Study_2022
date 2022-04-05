def DFS(y,x):
    global cnt
    cnt +=1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<n and 0<=nx<n:
            if blocks[ny][nx] == 1 and visited[ny][nx] == False:
                visited[ny][nx]=True
                DFS(ny,nx)

if __name__ =='__main__':
    n = int(input())
    blocks = []
    # visited = [[False]*n]*n    # 포인터라서 이렇게 만들면 안된다..
    visited = [[False] * n for _ in range(n)] ## 주의 할 것
    cnt = 0
    answer = []
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    for i in range(n):
        blocks.append(list(map(int, input().strip())))

    for j in range(n):
        for i in range(n):
            if blocks[j][i] == 1 and visited[j][i] == False:
                visited[j][i] = True
                cnt = 0
                DFS(j,i)
                answer.append(cnt)

    answer.sort()
    print(len(answer))
    for i in answer:
        print(i)
