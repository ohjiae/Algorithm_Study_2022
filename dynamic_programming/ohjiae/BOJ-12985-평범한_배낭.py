from sys import stdin
input = stdin.readline

N, K = list(map(int, input().split()))
# dp = {}

# for _ in range(N):
#     W, V = list(map(int, input().split()))
#     if V != 0 and W <= K:
#         if W in dp:
#             dp[W] = max(dp[W], V)
#         else: dp[W] = V
#
# mv = max(dp.values())
# for w in dp.keys():
#     if K-w in dp:
#         mv = max(dp[K-w]+dp[w], mv)
# print(mv)


dp = []
for _ in range(N):
    W, V = list(map(int, input().split()))
    if V != 0 and W <= K:
            dp.append((W, V))
