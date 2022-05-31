import sys
import heapq as hq
hl = []
for i in range(int(input())):
    x = int(sys.stdin.readline().rstrip())
    if x == 0 :
        print(hq.heappop(hl)[1] if hl else 0)
    else : hq.heappush(hl,(abs(x),x))