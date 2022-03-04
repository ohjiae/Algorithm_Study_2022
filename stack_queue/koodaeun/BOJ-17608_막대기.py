import sys

N = int(sys.stdin.readline()) # 입력할 막대기 개수
stick = []
count = 1 # 보이는 막대기, 1부터 시작

for i in range(N):
    stick.append(int(sys.stdin.readline()))

now = stick.pop() # 제일 높은 막대기
for i in range(N-1):
    nextStick = stick.pop() # 현재 막대기의 높이

    if nextStick > now:
        count += 1
        now = nextStick

print(count)