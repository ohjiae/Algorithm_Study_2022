import heapq
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
jewel = [list(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
jewel.sort()
bags.sort()
temp = []
result = 0

for bag in bags:
    while jewel and bag >= jewel[0][0]:
        heapq.heappush(temp, -jewel[0][1])  # 최대힙
        heapq.heappop(jewel)
    if temp:
        result += heapq.heappop(temp)
    elif not jewel:
        break

print(-result)