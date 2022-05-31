import heapq

def solution(jobs):
    leng = len(jobs)
    total, now = 0, 0
    queue = []
    jobs.sort(reverse=True)

    while jobs:
        # enqueue
        while jobs:
            if jobs[-1][0] > now:
                break
            x = jobs.pop()
            heapq.heappush(queue, (x[1], x[0]))
        
        # dequeue
        if queue:
            this = heapq.heappop(queue)
            now+=this[0]
            total+=now-this[1]
        else:
            now=jobs[-1][0]
        
    while queue:
        this = heapq.heappop(queue)
        now+=this[0]
        total+=now-this[1]
        
    
    return total//leng