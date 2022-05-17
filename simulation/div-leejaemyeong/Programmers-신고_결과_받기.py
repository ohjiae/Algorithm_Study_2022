def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)
    reporter={x:0 for x in id_list}
    
    for i in report:
        reporter[i.split()[1]]+=1
    
    for i in report:
        if reporter[i.split()[1]]>=k:
            answer[id_list.index(i.split()[0])]+=1
    
    return answer