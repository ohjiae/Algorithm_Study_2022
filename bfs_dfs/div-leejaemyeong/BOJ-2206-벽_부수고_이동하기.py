from collections import deque

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input())))

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs():
    deq=deque()
    deq.append([0,0,0])
    visited[0][0][0]=1

    while deq:
        x,y,wall=deq.popleft()
        if x==n-1 and y==m-1:
            return visited[x][y][wall]

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny][wall]==0:
                if arr[nx][ny]==0:
                    deq.append([nx,ny,wall])
                    visited[nx][ny][wall]=visited[x][y][wall]+1

                if wall==0 and arr[nx][ny]==1:
                    deq.append([nx,ny,1])
                    visited[nx][ny][1]=visited[x][y][wall]+1

    return -1

print(bfs())