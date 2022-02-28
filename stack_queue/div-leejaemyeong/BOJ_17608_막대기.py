import sys

input=sys.stdin.readline
stack=[]
for _ in range(int(input())):
    stack.append(int(input()))

max=0
cnt=0
while stack:
    a=stack.pop()
    if max<a:
        cnt+=1
        max=a
print(cnt)