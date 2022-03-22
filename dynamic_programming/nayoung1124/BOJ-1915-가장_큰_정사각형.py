n,m = map(int,input().split())
boxes = []
dp = [[0]*m for _ in range(n)]
answer = 0
for _ in range(n):
    boxes.append(list(map(int, list(input().rstrip()))))

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            dp[i][j] = boxes[i][j]
        elif boxes[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(dp[i][j], answer)

print(answer * answer)
