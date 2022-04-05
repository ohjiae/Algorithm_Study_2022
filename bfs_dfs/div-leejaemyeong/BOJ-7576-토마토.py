from collections import deque

dxy=[[1,0],[0,1],[-1,0],[0,-1]]

M,N=map(int,input().split())
arr=[]
deq=deque()


def bfs():
    max=0
    while deq:
        x,y=deq.popleft()
        for i in dxy:
            nx=x+i[0]
            ny=y+i[1]

            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny]==0:
                    deq.append([nx,ny])
                    arr[nx][ny]=arr[x][y]+1
                    if max<arr[nx][ny]:
                        max=arr[nx][ny]
    for a in arr:
        if 0 in a:
            return -1
    return max-1

for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j]==1:
            deq.append([i,j])
check=False
for i in arr:
    if 0 in i:
        check=True
        break
if check:
    ans=bfs()
    print(ans)
else:
    print(0)

