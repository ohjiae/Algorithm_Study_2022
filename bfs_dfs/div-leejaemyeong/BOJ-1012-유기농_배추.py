#DFS

import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    arr[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m:
            if arr[nx][ny]==1:
                dfs(nx,ny)

for _ in range(int(input())):
    cab = []
    m,n,k=map(int, input().split())
    arr=[[0]*m for _ in range(n)]

    for _ in range(k):
        x,y=map(int, input().split())
        arr[y][x]=1
        cab.append([y,x])
    cnt=0
    for i in cab:
        if arr[i[0]][i[1]]==1:
            dfs(i[0],i[1])
            cnt+=1
    print(cnt)



#BFS

import sys
from collections import deque

input=sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    deq=deque()
    deq.append([x,y])
    arr[x][y]=0
    while deq:
        x,y=deq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny]==1:
                    deq.append([nx,ny])
                    arr[nx][ny]=0


for _ in range(int(input())):
    cab=[]
    m,n,k=map(int, input().split())
    arr=[[0]*m for _ in range(n)]

    for _ in range(k):
        x,y=map(int, input().split())
        arr[y][x]=1
        cab.append([y,x])
    cnt=0
    for i in cab:
        if arr[i[0]][i[1]]==1:
            bfs(i[0],i[1])
            cnt+=1
    print(cnt)