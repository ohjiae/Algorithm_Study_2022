n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(map(int, input())))

dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
lens=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            dp[i+1][j+1]=min(dp[i+1][j],dp[i][j+1],dp[i][j])+1

            if dp[i+1][j+1]>lens:
                lens=dp[i+1][j+1]
print(lens**2)
