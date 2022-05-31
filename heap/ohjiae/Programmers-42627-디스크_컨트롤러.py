from collections import deque as dq
def solution(jobs):
    hl = len(jobs)
    jobs = dq(sorted(jobs))
    wait = [jobs.popleft()]
    time = 0
    answer = 0
    while wait:
        now = wait.pop()
        if now[0] <= time : #이전 업무 끝나기 전에 들어온 요청일때 (현재:3초, 3초전에 들어온 요청)
            answer += time - now[0] + now[1] #총작업시간 = (현재시간-요청한시간=기다린시간) + 작업시간
            time += now[1] #끝나는시간 = 현재 + 작업시간
        else : # 이전업무 끝난 후에 들어온요청일때 (이전업무:3초에 끝남, 다음업무: 18초에 들어옴)
            answer += now[1] #총 작업시간 += 순수 작업시간만 추가
            time = now[0]+now[1] #끝나는 시간 = 시작시간+작업시간

        while len(jobs)!=0 and jobs[0][0] <= time: #지금 작업이 끝날때쯤 이미 들어온 요청들 모두* 미리 대기열에 추가
            wait.append(jobs.popleft())

        if len(wait)==0 and len(jobs)!=0: #현재작업이 끝났는데 아직 요청목록 남아있는경우 요청시간빠른 하나만 가져옴.
            wait.append(jobs.popleft())
        wait.sort(key = lambda x : x[1],reverse=True) # 대기열 -> 작업시간 적은순정리, 젤 짧게 걸리는거 = 가장오른쪽
    return answer//hl