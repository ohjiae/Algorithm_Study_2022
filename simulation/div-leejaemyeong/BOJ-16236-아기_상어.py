import sys
from collections import deque

N=int(input())
arr=[]

shark_x,shark_y=0,0 # 상어의 위치
shark_size=2 # 상어의 크기
eat_cnt=0 # 상어가 먹은 물고기 수
fish_cnt=0 # 물고기 수
time=0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(N):
    arr.append(list(map(int,input().split())))
    for j in range(N):
        # 상어의 좌표 저장
        if arr[i][j]==9:
            shark_x,shark_y=i,j
            arr[i][j]=0
        #물고기의 갯수 카운팅
        elif 0<arr[i][j]<=6:
            fish_cnt+=1

def BFS(shark_x,shark_y):
    vis = [[False for _ in range(N)] for _ in range(N)]
    deq=deque()
    deq.append([shark_x,shark_y,0])
    vis[shark_x][shark_y]=True
    #먹을 수 있는 물고기까지의 최단거리 저장할 변수
    min_dis=sys.maxsize
    #물고기의 좌표와 거리 저장
    fish_list=[]
    while deq:
        x,y,dis=deq.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and not vis[nx][ny]:
                #이동할 곳이 shark_size보다 작거나 같으면 이동할 수 있으므로
                #해당 좌표의 vis배열 True로 변경
                if arr[nx][ny]<=shark_size:
                    vis[nx][ny]=True
                    #이동한 곳이 0보다 크고 shark_size보다 작으면 먹을 수 있는
                    #물고기이므로 min_dis에 이동거리 저장
                    if 0<arr[nx][ny]<shark_size:
                        #이동거리가 min_dis보다 크면 최단거리가 아니기 때문에 pass
                        if min_dis>=dis+1:
                            min_dis=dis+1
                            #최단거리의 물고기 좌표, 거리 저장
                            fish_list.append((nx,ny,dis+1))
                    #이동할 좌표의 값이 0이고 이동거리가 min_dis보다 작으면 아직
                    #먹을 수 있는 물고기를 찾지 못했기 때문에 deq에 해당 좌표,거리 저장
                    if dis+1<min_dis:
                        deq.append([nx,ny,dis+1])
    #만약 fish_list에 데이터가 들어있으면 최단거리에 먹을 수 있는
    #물고기를 찾았기 때문에 해당 배열을 내림차순 정렬해준다.
    #(내림차순 정렬하면 x좌표가 작은 순, 만약 같으면 y좌표가 작은순으로 저장됨)
    #이때 이동거리는 모두 최단거리만 저장되어 따로 정렬에 영향을 끼치지 않음
    if fish_list:
        fish_list.sort()
        print(fish_list)
        #가장 위에 있고 가장 왼쪽에 있는 최단거리의 먹을 수 있는 물고기를 반환
        return fish_list[0]
    else:
        return False



while fish_cnt:
    result=BFS(shark_x,shark_y)
    if not result:
        break
    shark_x,shark_y=result[0],result[1]
    time+=result[2]
    eat_cnt+=1
    fish_cnt-=1
    if shark_size==eat_cnt:
        shark_size+=1
        eat_cnt=0
    arr[shark_x][shark_y]=0

print(time)

