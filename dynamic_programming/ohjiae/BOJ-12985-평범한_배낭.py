from sys import stdin

input = stdin.readline

N, K = list(map(int, input().split()))
dp = {}
mv = 0
for _ in range(N):
    W, V = list(map(int, input().split()))
    if V != 0 and W <= K:
        if W in dp:
            dp[W] = max(dp[W], V)
        else:
            dp[W] = V
        if dp[K-W] in dp:
            mv = max(dp[K-W]+dp[W], mv)

print(max(dp.values()))
