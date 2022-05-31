def get_idx(genre, idx):
    for i in range(len(idx)):
        if idx[i][1] == genre: return i
    return None

def make_idx(genres, plays):
    res = []
    for i in range(len(genres)):
        check = False
        for j in range(len(res)):
            if res[j][1] == genres[i]:
                res[j][0] += plays[i]
                check = True
                break
        if not check: res.append([plays[i], genres[i]])
    return sorted(res, reverse=True)

def solution(genres, plays):
    idx = make_idx(genres, plays)

    res = [[] for _ in range(len(idx))]
    for i in range(len(plays)):
        res_idx = get_idx(genres[i], idx)
        res[res_idx].append((-plays[i], i))

    for i in range(len(idx)):
        res[i] = sorted(res[i])

    answer = []
    for i in range(len(idx)):
        for j in range(len(res[i])):
            if j == 2: break
            answer.append(res[i][j][1])
    return answer