import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
m=int(input())
dp=[[False]*n for i in range(n)]
for idx in range(n):
    for start in range(n):
        end=start+idx
        if end>=n:
            break
        if idx==0:
            dp[start][end]=True
        elif idx==1:
            if nums[start]==nums[end]:
                dp[start][end]=True
        elif nums[start]==nums[end] and dp[start+1][end-1]:
            dp[start][end]=True

for i in range(m):
    x,y=map(int,input().split())
    if dp[x-1][y-1]:
        print(1)
    else:
        print(0)
