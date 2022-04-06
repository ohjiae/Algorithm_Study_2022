from collections import deque
def bfs():
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    while starts:
        ey,ex = starts.popleft()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex+dx[k]
            if 0<=ny<N and 0<=nx<M:
                if boxes[ny][nx] == 0:
                    boxes[ny][nx]= boxes[ey][ex]+1
                    starts.append((ny,nx))




if __name__ == '__main__':
    M,N = map(int, input().split())
    answer = []
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    boxes=[]
    starts = deque()
    cnt = 0
    for i in range (N):
        boxes.append(list(map(int,input().split())))

    for i in range(M):
        for j in range(N):
            if boxes[j][i] == 1:
                starts.append((j,i))

    bfs()

    for i in boxes:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        cnt = max(cnt,max(i))
    print(cnt-1)
