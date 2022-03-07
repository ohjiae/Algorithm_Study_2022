import sys
from collections import deque
n,k = map(int, sys.stdin.readline().split())
que = deque([i for i in range(1,n+1)])
yose = deque()
cnt = 0
while que:
    temp = que.popleft()
    cnt += 1
    if k == cnt:
        yose.append(temp)
        cnt = 0
    else:
        que.append(temp)

print('<', end='')
print(*yose,sep=', ',end='')
print('>')