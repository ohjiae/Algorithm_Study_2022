import sys
from collections import deque


def bfs():
    while queue:
        temp = queue.popleft()
        for next_v in graph[temp]:
            if ans[next_v] == 0:
                ans[next_v] = temp
                queue.append(next_v)


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n+1)]
    for _ in range(1, n):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    queue = deque()
    queue.append(1)
    ans = [0] * (n+1)
    bfs()
    print(*ans[2:], sep='\n')
