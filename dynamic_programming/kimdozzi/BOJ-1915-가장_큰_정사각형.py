import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []
dp = [[0] * m for _ in range(n)]
ans = 0

for _ in range(n) :
    arr.append(list(map(int,input().rstrip())))

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:  # 사각형 외각
            dp[i][j] = arr[i][j]
        elif arr[i][j] == 0:  # 값이 0일 경우
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 #사각형의 외각이 아니고, 내부의 값이 1일 경우
        ans = max(dp[i][j], ans)

print(ans * ans)