from collections import deque

def solution(priorities, location):
    cnt = 0
    queue = deque()
    for i, v in enumerate(priorities):
        queue.append((i, v))

    while queue:
        max_value = max(queue, key=lambda x:x[1])[1]
        idx, value = queue.popleft()
        
        if value==max_value:
            cnt+=1
            if idx == location:
                break
        else:
            queue.append((idx, value))
            
    return cnt