import heapq

# 주의할 점 !
# 스코빌의 길이가 1과 2일경우


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K and scoville:
        if len(scoville) < 2:
            return -1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        temp = a + (b * 2)
        answer += 1
        heapq.heappush(scoville, temp)
    return answer


if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7

    print(solution(scoville, K))
