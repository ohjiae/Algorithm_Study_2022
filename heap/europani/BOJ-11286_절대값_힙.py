import sys
import heapq
input=sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    m = int(input())
    if m ==0:
        print(heapq.heappop(queue)[1] if queue else 0)
    else:
        heapq.heappush(queue, (abs(m), m))