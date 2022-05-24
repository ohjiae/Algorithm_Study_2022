import heapq

def check(pq, k):
    if pq[0] > k: return True
    return False

def mix(pq):
    if len(pq) < 2: return None
    first = heapq.heappop(pq)
    second = heapq.heappop(pq)
    third = first + second * 2
    
    heapq.heappush(pq, third)
    return pq

def solution(scoville, k):
    heapq.heapify(scoville)
    
    cnt = 0
    while not check(scoville, k):
        scoville = mix(scoville)
        if scoville == None: return -1
        cnt += 1
    return cnt