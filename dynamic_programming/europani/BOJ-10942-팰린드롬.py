import sys
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [[0] * (n+1) for _ in range(n+1)]

# 길이 1, 2 초기화
for i in range(1, n+1):
    dp[i][i]=1
    if i < n:
        if nums[i] == nums[i+1]:
            dp[i][i+1]=1

# 길이 3 이상
for leng in range(2, n):
    for idx in range(1, n-leng+1):
        if dp[idx+1][idx+leng-1] == 1 and nums[idx]==nums[idx+leng]:
            dp[idx][idx+leng]=1

m = int(input())
for _ in range(m):
    left, right = map(int, input().split())
    print(dp[left][right])