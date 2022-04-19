from collections import deque
from sys import stdin
input = stdin.readline
lines = []
for _ in range(int(input())):
    inp = list(map(int,input().split()))
    s,e = min(inp), max(inp)
    lines.append((s,e,e-s))
d = int(input())

def chk(li):
    li.sort(key = lambda x : x[1])
    cnt = {}
    for l in li:
        if l[2] < d:
            #pin = li[0][0]+d
            if l[1] in cnt:
                cnt[pin] += 1
    if len(cnt?조건문 확인할것)==0: print(0)
