from collections import deque
N, K = map(int,input().split())
q = deque(range(1,N+1))
if N < 3:
        print('<','2, 1' if N == 2 else 1,'>',sep='')
else: 
    res = []
    for i in range(1,N+1):
        q.rotate(-K+1)
        res.append(str(q.popleft()))
    print('<'+', '.join(res)+'>')
