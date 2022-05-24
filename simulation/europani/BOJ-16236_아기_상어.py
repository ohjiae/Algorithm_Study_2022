from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
sec, cnt, baby_size = 0, 0, 2
baby = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def get_fishes(ix, iy):
    fishes = []
    queue = deque()
    distance = [[-1] * n for _ in range(n)]
    distance[ix][iy]=0
    queue.append([ix, iy])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if graph[nx][ny] <= baby_size and distance[nx][ny]==-1:
                distance[nx][ny]=distance[x][y]+1
                queue.append([nx, ny])
                if graph[nx][ny] < baby_size and graph[nx][ny] != 0:
                    fishes.append([distance[nx][ny], nx, ny])

    return sorted(fishes)

# baby 이동
def move(fish):
    global sec, cnt, baby_size
    dist, x, y = fish
    sec+=dist  
    cnt+=1
    graph[baby[0]][baby[1]], graph[x][y] = 0, 9
    baby[0], baby[1] = x, y

    # level check
    if cnt == baby_size:
        baby_size+=1
        cnt=0

# init baby position
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            baby+=[i, j]

while True:
    fishes = get_fishes(baby[0], baby[1])

    if len(fishes) == 0:
        break
    move(fishes[0])

print(sec)