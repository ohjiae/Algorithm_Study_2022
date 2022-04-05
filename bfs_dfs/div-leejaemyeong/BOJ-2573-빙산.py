#pypy3

from collections import deque

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

dxy=[(1,0),(-1,0),(0,1),(0,-1)]


def bfs(x,y,vis,melt):

    deq=deque()
    deq.append([x,y])
    vis[x][y]=True
    while deq:
        x,y=deq.popleft()
        for i in range(4):
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    melt[x][y]-=1
                elif not vis[nx][ny]:
                    vis[nx][ny]=True
                    deq.append([nx,ny])


day=0
cnt=0
while True:
    vis = [[False for _ in range(m)] for _ in range(n)]
    melt = [[0 for _ in range(m)] for _ in range(n)]

    day+=1
    ch=False
    for i in range(n):
        for j in range(m):
            if arr[i][j]!=0 and not vis[i][j]:
                ch=True
                bfs(i,j,vis,melt)
                cnt+=1

    if cnt>=2:
        print(day-1)
        break
    elif cnt==0:
        print(0)
        break
    else:
        cnt=0

    for i in range(n):
        for j in range(m):
            arr[i][j]+=melt[i][j]
            if arr[i][j]<0:
                arr[i][j]=0