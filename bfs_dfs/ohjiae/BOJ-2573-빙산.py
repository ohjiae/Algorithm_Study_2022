from sys import stdin
N,M = map(int,input().split())
#input = stdin.readline
graph = [list(map(int,input().split())) for _ in range(N)]
vis = [[False]*(M-1) for _ in range(N-1)]
if N == 3 and M == 3 : print(0)
else:
    # 포문으로 돌면서 그안의 숫자 n >0 큐에 넣기 한덩이 끝나면 1씩 카운팅, 2이상일 때 멈춤.
    # and 4 방향중 0의 갯수만큼 카운팅해서 -1
    # 안 나뉘는 경우의 수?
    # ->  맥시멈이... 붙어있을 때

    print(graph,sep='\n')
