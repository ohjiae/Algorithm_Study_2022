def solution(id_list, report, k):
    answer = []
    result = {id: [0, set()] for id in id_list}
    for rpt in report:
        who, whom = rpt.split()
        if whom not in result[who][1]:
            result[who][1].add(whom)
            result[whom][0] += 1

    for id in id_list:
        cnt = 0
        for p in result[id][1]:
            if result[p][0] >= k:
                cnt += 1
        answer.append(cnt)
    return answer