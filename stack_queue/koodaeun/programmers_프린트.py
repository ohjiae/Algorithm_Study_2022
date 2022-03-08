def solution(priorities, location):

    answer = 0

    while len(priorities):
        for i in range(len(priorities)):
            if priorities[i] == max(priorities):
                answer += 1
                priorities[i] = 0
                if i == location:
                    return answer