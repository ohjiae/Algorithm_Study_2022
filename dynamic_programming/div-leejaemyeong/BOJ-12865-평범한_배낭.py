n,k=map(int, input().split())
wv=[(0,0)]
dp=[[0]*(k+1) for i in range(n+1)]
for _ in range(n):
    x,y=map(int, input().split())
    wv.append((x,y))


for i in range(1,n+1):
    for j in range(1,k+1):
        if j>=wv[i][0]:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-wv[i][0]]+wv[i][1])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][k])