import sys
input = sys.stdin.readline

n = int(input().rstrip())

apt = []
for i in range(n):
    apt.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global count  # global 전역변수 선언(아파트 수 세어주기 위함)

    if x <= -1 or x >= n or y <= -1 or y >= n:  #범위를 벗어나는 경우 종료조건 설정
        return False

    #탐색하는 원소가 1인 경우(아파트 단지를 생성할 수 있는 경우), 현재 위치를 아직 방문하지 않았다면
    if apt[x][y] == 1:
        count += 1      #이어진 집들끼리 count해준다, 123456712345678...

        apt[x][y] = -1  #방문처리

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            dfs(nx, ny)

        return True
    return False    #1이 아닌 부분에서는 False를 반환하게 함


num = []
global count
count = 0
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:   #만약 해당 위치에서 dfs수행해서 방문처리가 됐다면, count한다.
            num.append(count)

            result += 1  #방문처리가 이루어지는 부분에서만 count를 수행한다
            count = 0   #단지 각각의 합을 알기 위한 것이므로 한 단지의 합을 구한 뒤에는 count를 0으로 초기화해준다
print(result)   #총 단지 수

num.sort()
for i in num:   #한 줄씩 출력
    print(i)