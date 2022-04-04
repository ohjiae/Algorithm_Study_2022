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
    W,V = list(map(int,input().split()))
    if V != 0 and W <= K:
        dp.append((W,V))
dp.sort(key=lambda x: x[0],-x[1])
bag = 0
for i in range(len(dp)):
    if K - dp[i][0] >= 0:
        K -= dp[i][0]
        bag += \

            dp[i][1]

def chk(num):
    if dp[num][0]<= K:
        K -=
    mv = max(dp[num][1], dp[num-1][1]+dp[num-2][1])
    return
