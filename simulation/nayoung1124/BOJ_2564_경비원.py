def coodi(N,M,target):
    if target[0] == 1:
        return [target[1],M]
    elif target[0] == 2:
        return [target[1],0]
    elif target[0] == 3:
        return [0, M-target[1]]
    elif target[0] == 4:
        return [N,M-target[1]]

def cal_dist_zero(N,M,target): #원점으로 시계방향으로 돌아오는 거리
    # 서쪽에 있으면
    if target[0] == 0:
        return target[1]
    # 북쪽에 있으면
    if target[1] == M:
        return M+target[0]
    # 동쪽에 있으면
    if target[0] == N:
        return M+N+M-target[1]
    # 남쪽에 있으면
    if target[1] == 0:
        return M+N+M+N-target[0]

if __name__ == '__main__':
    N,M = map(int, input().split()) # 가로 세로
    k = int(input()) # 상점 갯수
    half = N+M
    ans = 0
    stores = []
    for _ in range(k):
        stores.append(list(map(int, input().split())))
    start = list(map(int, input().split()))
    coodi_stores = []
    coodi_start = []
    for store in stores:
        coodi_stores.append(coodi(N,M,store))
    coodi_start = coodi(N,M,start)
    zero_start = cal_dist_zero(N, M, coodi_start)

    # Calculate distance
    for store in coodi_stores:
        # 같은 줄에 있으면 그냥 거리 계산
        if coodi_start[0] == store[0] == 0 or coodi_start[0] == store[0] == N:
            dist = abs(coodi_start[1]-store[1])
        elif coodi_start[0] == store[0] == 0 or coodi_start[0] == store[0] == M:
            dist = abs(coodi_start[0] - store[0])

        # (0,0)~store, (0,0)~start
        else:
            zero_store = cal_dist_zero(N,M,store)
            dist = abs(zero_store-zero_start)
        if dist <= half:
            ans += dist
        else:
            ans += 2*(N+M)-dist
    print(ans)
