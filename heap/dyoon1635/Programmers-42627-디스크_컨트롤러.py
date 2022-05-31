import heapq

def possible_job(jobs, possible, cur_time):
    while True:
        if jobs and jobs[0][0] <= cur_time:
            start, job = heapq.heappop(jobs)
            heapq.heappush(possible, [job, start])
        else:
            break
    return jobs, possible

def solution(jobs):
    n = len(jobs)
    heapq.heapify(jobs)
    possible = []

    cur_time = 0
    res = 0
    while jobs or possible:
        jobs, possible = possible_job(jobs, possible, cur_time)
        #print(jobs, possible)
        if not possible:
            cur_time = jobs[0][0]
            continue

        job, start = heapq.heappop(possible)
        if cur_time <= start:
            res += job
            cur_time = start + job
        else:
            res += (cur_time - start + job)
            cur_time += job
    return int(res / n)