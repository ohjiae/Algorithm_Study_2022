num=1
while True:
    s=input()
    if s[0]=='-':
        break
    stack=[]
    cnt=0
    for i in s:
        if i=='{':
            stack.append(i)
        elif i=='}':
            if not stack:
                stack.append('{')
                cnt+=1
            elif stack[-1]=='{':
                stack.pop()
    if stack:
        cnt+=len(stack)//2
    print(num,'. ',cnt,sep='')
    num+=1
