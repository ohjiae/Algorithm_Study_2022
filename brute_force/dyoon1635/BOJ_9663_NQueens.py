res = 0
N = int(input())
queens = [0] * N

def is_possible(x):
    for i in range(x):
        if (queens[i] == queens[x]) or \
            (abs(i - x) == abs(queens[i] - queens[x])):
            return False
    return True

def dfs(x):
    global res
    if x == N:
        res += 1
        return None

    for i in range(N):
        queens[x] = i
        if is_possible(x):
            dfs(x+1)

dfs(0)
print(res)