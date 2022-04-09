# 입력받기
from collections import deque
import sys
import copy
input = sys.stdin.readline
M, N = map(int,input().split())
graph = []
q = deque()
## 토마토 입력 받으면서 위치 큐에 넣기.
for row in range(N):
    graph.append(list(map(int,input().split())))
    for col in range(len(graph[row])):
        if graph[row][col] == 1:
            q.append((row,col))
def bfs(que):
    day = -1
    while que:
        # 같은일자 토마토들만 subq에 넣고, que 비워서 다음날 토마토 넣을 자리 만들어 day 카운팅.
        subq = copy.deepcopy(que)
        que.clear()
        day += 1
        while subq:
            tmt = subq.popleft()
            y = tmt[0]
            x = tmt[1]
            for i in [(0,-1),(0,1),(1,0),(-1,0)]:
                if 0<=y+i[0]<N and 0<=x+i[1]<M and graph[y+i[0]][x+i[1]] == 0:
                    que.append((y+i[0],x+i[1]))
                    graph[y+i[0]][x+i[1]] = 1
    # 토마토 0 남았는지 확인
    # 4592ms
    #print(day if all([all(i) for i in graph]) else -1)
    # 4484ms
    for i in graph:
        if not all(i):
            day = -1
            break
    print(day)
bfs(q)

