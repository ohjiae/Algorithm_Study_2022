import heapq
import sys

input=sys.stdin.readline
n,k=map(int, input().split())
jewel=[]
bag=[]

for _ in range(n):
    m,v=map(int, input().split())
    heapq.heappush(jewel,(m,v))


for _ in range(k):
    bag.append(int(input()))
bag.sort()

cost=0
jewel_2=[]
for b in bag:
    while jewel and b>=jewel[0][0]:
        heapq.heappush(jewel_2,-heapq.heappop(jewel)[1])
    if jewel_2:
        cost-=heapq.heappop(jewel_2)

print(cost)