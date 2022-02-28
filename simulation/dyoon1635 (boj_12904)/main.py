from collections import deque

if __name__ == "__main__":
    s = deque(input().rstrip())
    t = deque(input().rstrip())

    check = False
    while t:
        # s에서 연산을 통해 t를 만드는 경우를 모두 check시 tc에 걸릴 수 있으므로
        # 두 가지 연산을 역방향으로 구현. t -> s로 만드는 경우를 check
        # t -> s는 idx = -1에 따라 연산이 정해져 있음
        if t[-1] == 'A':
            t.pop()
        elif t[-1] == 'B':
            t.pop()
            t.reverse()

        if t == s:
            check = True
            break
    if check:
        print(1)
    else:
        print(0)