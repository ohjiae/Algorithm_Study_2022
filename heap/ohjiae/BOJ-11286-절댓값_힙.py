from collections import deque
heap = deque()
for _ in range(int(input())):
    x = int(input())
    heap.append(x)
    #데큐엔 sort가없는데..
    print(f'x={x},min={heap[0]}')
    if x == 0:
        if len(
                heap)==0:
            print(0)
        else :
            print(
                heap.popleft())