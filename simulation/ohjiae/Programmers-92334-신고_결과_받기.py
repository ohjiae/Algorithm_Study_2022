
def solution(id_list, report, k):
    result = {}
    warned = {}
    ban = set()
    answer = []
    # for id in id_list:
    #     result[id] = set()
    #     warned[id] = set()
    for res in report:
        reporter, whom = res.split(' ')
        result[reporter].add(whom)
        warned[whom].add(reporter)
    for b in warned:
        if len(b)>=k:
            ban.add(b)
    for id in id_list:
        answer.append(len(result[id].intersection(ban)))
    print(answer)
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)


def solution(id_list, report, k):
    result = {}
    ban = {}
    answer = []
    for id in id_list:
        result[id] = set()
        ban[id] = 0
    for res in report:
        reporter, whom = res.split(' ')
        if whom in result[reporter]:
            pass
        else:
            result[reporter].add(whom)
            ban[whom] += 1

    for a in id_list:
        for i in result[a]:

    return answer
    return answer

