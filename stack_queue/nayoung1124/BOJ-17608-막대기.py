import sys
if __name__ == '__main__':
    N = int(input())
    stack = list()
    ans = 1
    for _ in range (N):
        a = int(sys.stdin.readline().rstrip())
        stack.append(a)
    current = stack.pop()
    while stack:
        if current < stack[-1]:
            ans += 1
            current = stack[-1]
        else: stack.pop()
    print(ans)
