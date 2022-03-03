import itertools
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque()

    # setting queue((file_idx, priority))
    for name, prior in enumerate(priorities):
        queue.append((name, prior))

    while (queue):
        if len(queue) == 1:
            answer += 1
            break

        # Cannot print
        # itertools.islice: deque를 slice 하기 위해 사용
        if max(j[1] for j in list(itertools.islice(queue, 1, len(queue)))) > queue[0][1]:
            target = queue.popleft()
            queue.append(target)

        # Can print
        else:
            target = queue.popleft()
            answer += 1
            if target[0] == location:
                break

    return answer
