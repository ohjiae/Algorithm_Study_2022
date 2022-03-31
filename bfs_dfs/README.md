## DFS (Depth-First Search)
- 깊은 부분을 우선적으로 탐색하는 알고리즘
- **`스택`이나 `재귀함수` 이용**
- 모든 노드를 방문할 경우 사용한다
- 문제에 제한이 있는 경우 `가지치기`와 `백트래킹`으로 경우를 줄일 수 있다
- 재귀함수를 사용할 경우 <u>종료조건을 정확</u>하게 명시해야 한다 (Base Case)

![image](https://user-images.githubusercontent.com/48157259/143531695-149b14d7-52b6-4f05-b37e-8aa61dd92a40.png)

```python
v, e, s = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)


def dfs(v):
    print(v, end=' ')
    visited[v]=True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(s)
```



## BFS (Breath-First Search)
- 같은 레벨을 우선적으로 탐색하는 알고리즘
- **`큐` 이용**
- 노드 사이의 최단경로를 찾을 경우 사용한다

![image](https://user-images.githubusercontent.com/48157259/143531860-e4de6419-96bc-4b74-86dd-8f9f80a1e60a.png)

```python
from collections import deque

v, e, s = map(int, input().split())
graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    visited = [False] * (v+1)

    queue = deque([start])
    visited[start]=True

    while queue:
        now = queue.popleft()
        print(now, end=' ')

        for i in graph[now]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
bfs(s)
```

## DFS/BFS 비교

|DFS|BFS|
|:--:|:--:|
|스택 or 재귀함수|큐|
|모든노드 방문시 사용|최단경로|
|더 간단|더 복잡|
|느림|빠름|

### ◼︎ DFS와 BFS 선택 방법  
(1) 모든 정점을 방문하는 문제 : `DFS`와 `BFS` 모두 선택 가능  
(2) 경로의 특징을 저장하는 문제 : `DFS` 사용  
\- 각 정점에 숫자가 적혀있고 a~b경로에 같은 숫자가 있으면 안된다는 등 특징을 저장해야 하는 문제  
(3) 최단거리 문제 : 미로 찾기 등의 최단거리를 구하는 문제는 `BFS` 사용
