import heapq, sys

pq = []
n = int(input())
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if not pq: print(0)
        else:
            tmp = heapq.heappop(pq)
            print(tmp[0] * tmp[1])
    else:
        if x < 0: heapq.heappush(pq, [abs(x), -1])
        else: heapq.heappush(pq, [abs(x), 1])