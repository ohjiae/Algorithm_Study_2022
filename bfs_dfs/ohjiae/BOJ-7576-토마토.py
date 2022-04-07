# 입력받기
from collections import deque
import sys
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
    day = 0
    while que:
        tmt = que.popleft()
        y = tmt[0]
        x = tmt[1]
        for i in [(0,-1),(0,1),(1,0),(-1,0)]:
            if 0<=y+i[0]<N and 0<=x+i[1]<M and graph[y+i[0]][x+i[1]] == 0:
                que.append(graph[y+i[0]][x+i[1]])
                graph[y+i[0]][x+i[1]] = 1
        day += 1


bfs(q)