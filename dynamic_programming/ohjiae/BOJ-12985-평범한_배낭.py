from sys import stdin

input = stdin.readline

N, K = list(map(int, input().split()))
A = []
bag = 0
for _ in range(N):
    W, V = list(map(int, input().split()))
    if V != 0 and W <= K:
        AW = list(A[i][0] for i in range(len(A)))
        if W in AW:
            idx = AW.index(W)
            AW[idx] = (W,max(AW[idx][1], V))
        else: A.append((W, V))


