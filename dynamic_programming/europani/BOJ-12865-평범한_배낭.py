n, t = map(int, input().split())
dp = [0] * (t+1)

for _ in range(n):
    w, v = map(int, input().split())

    for i in range(t, w-1, -1):
        dp[i] = max(dp[i-w]+v, dp[i])
print(dp[t])    