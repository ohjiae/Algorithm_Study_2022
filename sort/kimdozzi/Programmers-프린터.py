from collections import deque
def solution(priorities, location) :
    Queue = deque([[v,i] for i,v in enumerate(priorities)])
    answer = 0

    while len(Queue) :
        temp = Queue.popleft()
        if Queue and max(Queue)[0] > temp[0] :
            Queue.append(temp)
        else:
            answer += 1
            if temp[1] == location :
                break
    return answer

priorities = [1,1,9,1,1,1]
location = 0

print(solution(priorities,location))

