import math
from collections import deque

n,m=map(int, input().split())
k=int(input())
arr=deque()
for i in range(k+1):
    x,y=map(int,input().split())
    if x==1:
        arr.append((0,y))
    elif x==2:
        arr.append((m,y))
    elif x==3:
        arr.append((y,0))
    elif x==4:
        arr.append((y,n))

dis=0
nx,ny=arr.pop()
while arr:
    x,y=arr.pop()
    if x==0 or x==m:
        if nx==x:
            dis+=abs(ny-y)
        elif ny==0 or ny==n:
            dis+=abs(nx-x)+abs(ny-y)
        else:
            dis+=m+min((y+ny),(2*n-y-ny))
    elif y==0 or y==n:
        if ny==y:
            dis+=abs(nx-x)
        elif nx==0 or nx==m:
            dis+=abs(nx-x)+abs(ny-y)
        else:
            dis+=n+min((x+nx),(2*m-x-nx))
print(dis)
