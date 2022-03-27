from collections import deque, defaultdict
def DFS(graph, root):
    stack = [root]
    visited = []
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            k = sorted(graph[n], reverse=True)
            stack.extend(k)
    return visited

def BFS(graph, root):
    q = deque()
    q.append(root)
    visited = []
    while q:
        m = q.popleft()
        if m not in visited:
            visited.append(m)
            tmp = sorted(graph[m])
            q.extend(tmp)
    return visited

if __name__ =='__main__':
    n, m, root = map(int, input().split())
    graph = defaultdict(list)
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    print(*DFS(graph,root))
    print(*BFS(graph, root))
