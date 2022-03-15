import sys

input=sys.stdin.readline
n=int(input())
time=[]
for _ in range(n):
    time.append(list(map(int, input().split())))
time.sort(key=lambda x:(x[1],x[0]))
cnt=1
end=time.pop(0)[1]
for i in time:
    if end<=i[0]:
        cnt+=1
        end=i[1]
print(cnt)