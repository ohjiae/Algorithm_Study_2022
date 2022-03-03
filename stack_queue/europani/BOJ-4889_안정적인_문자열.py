import sys
input = sys.stdin.readline
order = 0

while True:
    order+=1
    string = input().rstrip()
    if '-' in string:
        break

    stack = []
    cnt=0
    for x in string:
        if stack:    
            if x == '{':
                stack.append('{')
            else:
                stack.pop()
        else:
            stack.append('{')
            if x == '}':
                cnt+=1

    if stack:
        cnt+=len(stack)//2

    print(f'{order}. {cnt}')