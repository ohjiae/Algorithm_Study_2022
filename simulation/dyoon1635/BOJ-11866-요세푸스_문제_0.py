from collections import deque

def Josephus(dq, k):
    print('<', end='')
    while True:
        for i in range(k - 1):
            dq.rotate(-1)
        num = dq.popleft()
        print(num, end='')
        if not dq: break
        print(', ', end='')
    print('>')

def main():
    n, k = map(int, input().split())
    dq = deque(range(1, n + 1))
    Josephus(dq, k)

if __name__ == "__main__":
    main()