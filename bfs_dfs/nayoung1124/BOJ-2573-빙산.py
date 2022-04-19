from collections import deque
from copy import deepcopy
def bfs(boxes,dx,dy,visited,i,j,N,M):
    que = deque()
    que.append((i, j))
    while que:
        ex,ey = que.popleft()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex+dx[k]
            if 0<=nx<N and 0<=ny<M:
                if boxes[nx][ny] !=0 and visited[nx][ny]==0:
                    visited[nx][ny] = 1
                    que.append((nx,ny))
    return visited


def one_year(boxes_,dx,dy):

    for i in range(1,N-1):
        for j in range(1,M-1):
            if boxes[i][j]!=0:
                cnt_empty = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if boxes[nx][ny]==0:
                        cnt_empty+=1
                boxes_[i][j]=boxes[i][j]-cnt_empty
                if boxes_[i][j]<0:
                    boxes_[i][j]=0
    return boxes_

if __name__ == '__main__':
    N,M = map(int, input().split())
    answer = []
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    boxes=[]
    cnt = 0

    for i in range (N):
        boxes.append(list(map(int,input().split())))

    
    while sum(sum(boxes,[]))!=0:
        end_flag = False
        visited = [[0] * M for _ in range(N)]
        ice = 0
        for i in range(N):
            for j in range(M):
                if boxes[i][j] != 0 and visited[i][j] == 0:
                    visited[i][j] = 1
                    ice += 1
                    visited = bfs(boxes,dx,dy,visited,i,j,N,M)
        if ice > 1:
            end_flag = True
            print(cnt)
            break

        cnt+=1
        boxes_ = deepcopy(boxes)
        boxes = one_year(boxes_,dx,dy)

    if end_flag == False:
        print(0)


