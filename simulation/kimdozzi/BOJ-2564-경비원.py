'''
결론부터 말하자면, 풀지 못하였다. 
첫번째 시도는 2차원 배열을 이용하여 최단거리를 구하려고 하였다. 하지만 주어진 row, col안에서 이동이 불가능하기 때문에 
아주 번거로웠고, 어렵게 생각한 방식이였다. 
두번째 시도는 덱을 사용하여 각 위치를 넣고 distance를 구하는 함수에서 동근이의 위치를 기준으로 각 상점의 위치를 계산하려고 하였다.
문제를 풀면 풀수록 생각할 조건이 많아지고 동,서,남,북의 모든 케이스에서 상점의 위치를 고려하니 헷갈리고 내가 풀면서도 무슨 말인지 이해가 안갈
정도의 코드였다. 그러고 스터디원에게 도움을 요청하여서 소스코드를 참고하였다. 보고 있으니 계속 따라만 하게되어서 다시 접고 
새로 코드를 짰지만 ..! 이전에 본 소스코드가 머리에 멤돌아 따라적는 것 같았다. 그래서 포기하고 구글을 통해 쉽게 이해할만한 코드를 접하였다.
그것이 아래의 코드이다. 이 코드는 (0,0)의 좌표를 기준으로 시계방향, 반시계방향을 계산하였다. 아주.. 간단했다 
'''
import sys
input = sys.stdin.readline

def getDistance(x,y) :
    if x == 1: # 북
        return y
    if x == 2: # 남
        return w + h + w - y
    if x == 3: # 서
        return w + h + w + h - y
    if x == 4: # 동
        return w + y

if __name__=='__main__':
    w,h = map(int,input().split())
    N = int(input())

    store = []
    for _ in range(N+1) :
        x, y = map(int,input().split())
        store.append(getDistance(x,y))

    cnt = 0 # 최단거리 누적 합

    for i in range(N) : # 동근이와 상점 사이의 최단거리
        counterclockwise = abs(store[-1] - store[i]) #반시계방향
        clockwise = 2 * (w + h) - counterclockwise #시계방향
        cnt += min(counterclockwise,clockwise) #최단거리 구하기 

    print(cnt)

