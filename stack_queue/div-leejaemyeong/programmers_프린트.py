from collections import deque

def solution(priorities, location):
    order_prior=deque()
    for i in range(len(priorities)):
        order_prior.append((i,priorities[i]))
    cnt=0
    while order_prior:
        check=True
        order,prior=order_prior.popleft()
        for i in order_prior:
            if prior<i[1]:
                order_prior.append((order,prior))
                check=False
                break
        if check:
            cnt+=1
        if check and order==location:
            return cnt