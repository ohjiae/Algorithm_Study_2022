
def check(i):   # 세로, 대각선 중복 체크
    for j in range(i):
        if queen[i] == queen[j] or queen[i]-i == queen[j]-j or queen[i]+i == queen[j]+j:
            return False
    return True

def dfs(x):
    global result
    # Base Case
    if x == n:
        result+=1
        return

    for i in range(n):      # y좌표 탐색
        queen[x]=i
        if check(x):
            dfs(x+1)

n = int(input())
result = 0
queen = [-1] * n        # index : x좌표 / value : y좌표

dfs(0)
print(result)