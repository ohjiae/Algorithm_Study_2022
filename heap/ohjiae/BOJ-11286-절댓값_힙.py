import sys
import heapq as hq
# hl = []
# for i in range(int(input())):
#     x = int(sys.stdin.readline().rstrip())
#     if x == 0 :
#         print(hq.heappop(hl)[1] if hl else 0)
#     else : hq.heappush(hl,(abs(x),x))


import heapq

# 최소힙 리스트
heap_list = [3, 7, 1, 5, 9]
heapq.heapify(heap_list)

# 원소 삭제
heapq.heappop(heap_list)  # 리턴 후 삭제됨, list의 pop처럼.

# 확인
print(heap_list)