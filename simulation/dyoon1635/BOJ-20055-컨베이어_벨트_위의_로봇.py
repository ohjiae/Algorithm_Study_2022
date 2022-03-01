from collections import deque

# n : belt의 size, k : belt 종료 조건 (내구도 제한)
# belt : 각 idx는 해당 위치의 내구도를 의미
# robot : 각 robot이 위치한 belt의 idx
n, k = map(int, input().split())
belt = deque(map(int, input().split()))
robot = deque()
step = 0

def count_zero():
    # belt에서 내구도가 0인 부분 count
    # 내구도 제한(k)에 걸리면 False return
    cnt = 0
    for b in belt:
        if b == 0:
            cnt += 1
    if cnt >= k:
        return False
    return True

def step_1():
    # belt와 그 위에 있는 robot이 한 칸 시계 방향 회전
    # robot의 idx 1씩 더해주고,
    # 가장 앞의 robot이 내리는 위치 도달 시 deque에서 pop
    global step
    step += 1
    belt.rotate(1)
    if robot:
        for i in range(len(robot)):
            robot[i] += 1
        if robot[-1] >= n - 1:
            robot.pop()

def step_2():
    # 가장 먼저 올라간 robot부터 이동 조건 체크 후 이동
    # 이동 조건 : belt 내구도 > 0, 해당 idx에 robot 부재
    for i in reversed(range(len(robot))):
        cur = robot[i]
        if belt[cur + 1] and not cur + 1 in robot:
            robot[i] += 1
            belt[cur + 1] -= 1

        if robot[-1] >= n - 1:
            robot.pop()

def step_3():
    # 올리는 위치(belt의 idx = 0)의 내구도가 0이 아니라면 robot 올림
    # step 1에서 이미 rotate를 수행했으므로 0의 위치에 robot이 존재하는 경우는 배제
    if belt[0]:
        robot.appendleft(0)
        belt[0] -= 1

if __name__ == "__main__":
    while count_zero():
        step_1()
        step_2()
        step_3()
    print(step)