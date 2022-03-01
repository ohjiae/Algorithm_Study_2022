import sys
n = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for i in range(n)]
cnt = 1
temp = stack.pop()
for i in range(len(stack)) :
    compare = stack.pop()
    if temp < compare:
        cnt += 1
        temp = compare

print(cnt)
