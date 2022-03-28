import sys
n,m = sys.stdin.readline().split()
n = int(n)
m = int(m)

res = [[] for _ in range(n+2)]
for i in range(n+1):
    y = list(map(int,sys.stdin.readline().split()))
    cnt = 0
    for j in range(m+1):
        if y[j] == 1:
            if cnt == 0:
                sx = j
            cnt += 1
            if j == m-1:
                res[i][-1].append((cnt,sx,i))
        elif y[j] == 0 and cnt != 0:
            res[i][-1].append((cnt,sx,i))
            cnt = 0

print(res)
