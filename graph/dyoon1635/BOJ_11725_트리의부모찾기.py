from collections import deque

n = int(input())
tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for idx in tree[cur]:
        if parent[idx] == 0:
            parent[idx] = cur
            q.append(idx)

for i in range(2, n + 1):
    print(parent[i])