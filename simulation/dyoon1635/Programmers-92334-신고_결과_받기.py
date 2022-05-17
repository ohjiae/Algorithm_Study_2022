def get_idx(name, idx):
    for i in idx:
        if name == i[0]:
            return i[1]
    return -1

def solution(id_list, report, k):
    n = len(id_list)
    idx = []
    for i in range(n):
        idx.append((id_list[i], i))

    rep_res = [[0]*n for _ in range(n)]
    for i in range(len(report)):
        x, y = report[i].split()
        rep_res[get_idx(x, idx)][get_idx(y, idx)] = 1
    
    sanc_list = []
    for j in range(n):
        cnt = 0
        for i in range(n):
            cnt += rep_res[i][j]
        if cnt >= k: sanc_list.append(j)
        
    answer = [0] * n
    for i in range(n):
        for sanc in sanc_list:
            if rep_res[i][sanc] > 0: answer[i] += 1
    
    return answer