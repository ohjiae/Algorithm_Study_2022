import heapq

n = int(input())
lines_tmp =[sorted(map(int, input().split())) for _ in range(n)]
d = int(input())

lines = []
for line in lines_tmp:
    if line[1]-line[0]<= d:
        lines.append(line)
lines.sort(key=lambda x:x[1])

queue = []
result = 0
for line in lines:
    if not queue:
        heapq.heappush(queue, line)
        continue

    while queue and queue[0][0] < line[1]-d:   # 현재기준 철로: (line끝점-철로길이) ~ line끝점
        heapq.heappop(queue)        # 맨앞 line이 현재기준 철로에 미충족시 pop
    heapq.heappush(queue, line)
    result=max(len(queue), result)

print(result)