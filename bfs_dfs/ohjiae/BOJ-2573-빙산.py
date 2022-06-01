from sys import stdin
from collections import deque
N,M = map(int,input().split())
input = stdin.readline
graph = [list(map(int,input().split())) for _ in range(N)]
vis = [[False]*(M-1) for _ in range(N-1)]
q = deque()
move = [(0,-1),(0,1),(-1,0),(1,0)]
def chk(y,x):
    cnt = 0
    for i in move:
        if 0<=x+i[0]<M and 0<=y+i[1]<N and graph[y][x] == 0:
            cnt += 1
    graph[y][x] -= 1
cube = 0
def dfs(y,x,cube):
    for i in move:
        if 0<=x+i[0]<M and 0<=y+i[1]<N and graph[y][x] != 0:
            cube += 1
            if cube >= 2 :
                return cube
                break
            else: dfs(y+i[0],x+i[0],cube)

def chkcube(c):
    for row in range(1,N-1):
        for col in range(1,M-1):
            dfs(row,col,c)
    print('here',cube)
# 포문으로 돌면서 그안의 숫자 n >0 큐에 넣기 한덩이 끝나면 1씩 카운팅, 2이상일 때 멈춤.
def bfs():
    for row in range(1,N-1):
        for col in range(1,M-1):
            if graph[row][col]>0:
                # and 4 방향중 0의 갯수만큼 카운팅해서 -1
                q.append((row,col))
                chk(row,col)
                print(*graph,sep='\n')
                print('----')
    chkcube(0)
    # 안 나뉘는 경우의 수?
    # ->  맥시멈이... 붙어있을 때

if N == 3 and M == 3 : print(0)
else:
    chk()

