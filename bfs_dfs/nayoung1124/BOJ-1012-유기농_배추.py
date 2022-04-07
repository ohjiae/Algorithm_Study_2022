from collections import deque
def bfs(y,x):
    q = deque()
    q.append((y,x))
    while q:
        ey,ex = q.popleft()
        for k in range(4):
            nx = ex+dx[k]
            ny = ey+dy[k]
            if 0<=nx<N and 0<=ny<M:
                if blocks[ny][nx]==1 and visited[ny][nx]==False:
                    visited[ny][nx] =True
                    q.append((ny,nx))


if __name__ == '__main__':
    T = int(input())

    answer = []
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]
    for _ in range (T):
        # make map
        cnt = 0
        M, N, K = map(int, input().split())
        blocks = [[0]*N for i in range(M)]
        visited = [[False] * N for ___ in range(M)]
        for __ in range(K):
            m,n = map(int, input().split())
            blocks[m][n]=1
        #bfs
        for j in range(M):
            for i in range(N):
                if blocks[j][i] == 1 and visited[j][i] == False:
                    cnt+=1
                    visited[j][i]=True
                    bfs(j,i)
        print(cnt)
