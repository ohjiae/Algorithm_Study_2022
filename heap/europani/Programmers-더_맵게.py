import heapq

def solution(scoville, K):
    scoville.sort()
    cnt=0

    # mix
    while scoville[0] < K:
        if len(scoville) > 1:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)

            mixed = first + (second*2)
            cnt+=1
            heapq.heappush(scoville, mixed)
        else:
            return -1
    
    return cnt