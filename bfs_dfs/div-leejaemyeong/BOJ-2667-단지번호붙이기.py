# BFS

from collections import deque

n=int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

nums=[]

def bfs(x,y):
    num=1
    deq=deque()
    deq.append((x,y))
    arr[x][y]=0
    while deq:
        x,y=deq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
                deq.append((nx,ny))
                arr[nx][ny]=0
                num += 1
    nums.append(num)

cnt=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            bfs(i,j)
            cnt+=1
print(cnt)
nums.sort()
for i in nums:
    print(i)

##################################################
# BFS
n=int(input())

arr=[]
for i in range(n):
    arr.append(list(map(int,input())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]

nums=[]


def dfs(x,y):
    global num
    arr[x][y]=0
    num+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
            dfs(nx,ny)

cnt=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            num = 0
            dfs(i,j)
            nums.append(num)
            cnt+=1
print(cnt)
nums.sort()
for i in nums:
    print(i)