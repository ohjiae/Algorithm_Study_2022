'''
예전 풀이
def solution(priorities, location):
    from collections import deque
    q = deque([(p,i) for i,p in enumerate(priorities)])
    answer = 0
    
    while q:
        np = q.popleft()
        if q and max(q)[0] > np[0]:
            q.append(np)
        else :
            answer += 1
            if np[1] == location:
                break

    return answer
'''
from collections import deque
def solution(priorities, location):
    answer = 0
    printlist = deque((n,p) for n,p in enumerate(priorities))
    
    maxpr = max(printlist, key = lambda x:x[1])
    
    while printlist:
        tmp = printlist.popleft()
        if tmp[1] < maxpr[1]:
            printlist.append(tmp)
        else :
            answer += 1
            if tmp[0] == location:
                break
            maxpr = max(printlist, key = lambda x:x[1])
    return answer
