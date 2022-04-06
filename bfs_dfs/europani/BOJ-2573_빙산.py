import copy
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0
    

def melt(graph):
    new_graph = [[0]*m for _ in range(n)]
    for x in range(1, n-1):
        for y in range(1, m-1):
            if graph[x][y]!=0:
                cnt=0
                for i in range(4):
                    if graph[x+dx[i]][y+dy[i]]==0:
                        cnt+=1
                if graph[x][y]-cnt > 0:
                    new_graph[x][y] = graph[x][y]-cnt 
                  
    return new_graph

# graph의 최대값 출력
def check_zero(graph):
    return max(map(max, graph))
  
# 분리 확인
def check_chunk(graph):
    visited = copy.deepcopy(graph)
  
    def dfs(x, y):
        visited[x][y]=0
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
    
            if visited[nx][ny] != 0:
                dfs(nx, ny)

    for i in range(1, n-1):
        stop=False
        for j in range(1, m-1):
            if visited[i][j]!=0:
                dfs(i, j)
                stop=True
                break

        if stop: break

    if check_zero(visited) > 0:
        return False
    else:
        return True


while check_zero(graph) != 0:
    graph = melt(graph)
    result+=1

    if not check_chunk(graph):
        print(result)
        break
else:
    print(0)