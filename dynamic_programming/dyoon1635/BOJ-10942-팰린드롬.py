import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline())
    nums = [0] + list(map(int, sys.stdin.readline().split()))
    dp = [[False for _ in range(n+1)] for _ in range(n+1)] # dp[length][start_idx]

    for i in range(1, n):
        dp[1][i] = True
        if nums[i] == nums[i + 1]:
            dp[2][i] = True
    dp[1][n] = True

    for length in range(3, n + 1):
        for start_idx in range(1, n - length + 2):
            if nums[start_idx + length - 1] == nums[start_idx] \
                    and dp[length-2][start_idx+1]:
                dp[length][start_idx] = True

    for i in range(int(input())):
        s, e = map(int, sys.stdin.readline().split())
        sys.stdout.write(str(int(dp[e-s+1][s])) + '\n')