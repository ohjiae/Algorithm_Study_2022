# 1032
import sys
n = int(sys.stdin.readline())
lst = list(map(str,input().rstrip()))

while n > 1 :
    prompt = list(map(str,input().rstrip()))
    for i in range(len(prompt)) :
        if prompt[i].lower() or prompt[i] == '.':
            if len(lst) == len(prompt) and lst[i] != prompt[i]:
                lst[i] = '?'
            else :
                continue
        else:
            sys.exit(1)

    n -= 1
print(''.join(lst))