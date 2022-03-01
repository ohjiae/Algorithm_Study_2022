from collections import deque

def calculate(s):
    res = 0
    limit = 0
    while s:
        cur = s.pop()
        if cur > limit:
            res += 1
        limit = max(limit, cur)
    return res

def main():
    n = int(input())
    stick = deque()
    for _ in range(n):
        tmp = int(input())
        stick.append(tmp)
    print(calculate(stick))


if __name__ == "__main__":
    main()
