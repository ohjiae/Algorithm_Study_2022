import sys
INF = sys.maxsize

n = int(input())
dp = [INF] * (n+1)
dp[0] = 0

for i in range(2, n+1):
    if i%5 == 0:
        dp[i] = i//5
    if i%2 == 0:
        dp[i] = min(i//2, dp[i-2]+1, dp[i])
    else:
        dp[i] = min(dp[i-2]+1, dp[i])
print(dp[n] if dp[n] != INF else -1)