import sys
import heapq

n = int(input())
lst = []
for _ in range(n):
    value = int(sys.stdin.readline())
    if value:
        heapq.heappush(lst, [abs(value), value])
    else:
        if not lst:
            print(0)
            continue
        print(heapq.heappop(lst)[1])
