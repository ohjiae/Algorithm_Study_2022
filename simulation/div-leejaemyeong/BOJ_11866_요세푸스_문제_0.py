from collections import deque
 
n,k=map(int, input().split())
ans=[]
deq=deque()
for i in range(1,n+1):
    deq.append(i)
 
 
while deq:
    deq.rotate(-k)
    ans.append(deq.pop())
print('<',', '.join(str(i) for i in ans),'>',sep='')