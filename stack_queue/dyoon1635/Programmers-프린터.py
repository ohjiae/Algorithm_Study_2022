from collections import deque

def solution(pr, loc):
    answer = 0
    pr = deque(pr)

    # check : 내가 요청한 문서의 위치 표시
    check = deque([False]*len(pr))
    check[loc] = True
    
    while True:
        if pr[0] < max(pr):
            # 맨 앞의 문서가 priority에서 밀리면
            # 대기열의 마지막으로 보냄
            pr.rotate(-1)
            check.rotate(-1)
        else:
            # 맨 앞의 문서가 priority가 가장 높다면 인쇄
            # 내가 요청한 문서라면 종료.
            answer += 1
            if check[0]:
                break
            pr.popleft()
            check.popleft()
    return answer