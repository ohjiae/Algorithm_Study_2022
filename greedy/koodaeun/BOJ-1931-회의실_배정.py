import sys

n = int(sys.stdin.readline().rstrip())

time = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time.append((s, e))

time.sort()                     #시작시간 기준 오름차순 정렬
time.sort(key=lambda x:x[1])    #종료시각(e) 기준 오름차순 정렬

room = 1
end_time = time[0][1]           #첫번째 회의의 끝나는 시각

for i in range(1, n):               # ex. 1번째 회의의 끝나는 시각과 2번째 회의의 시작하는 시각을 비교 2번째 회의의 시작 시각이 더 크다면
    if time[i][0] >= end_time:
        room += 1                   #사용할 수 있는 회의로 판단, room 을 +1해줌
        end_time = time[i][1]       #ex.end_time을 1번째 회의의 끝나는 시각에서 2번째 회의의 끝난는 시각으로 바꿔줌
print(room)