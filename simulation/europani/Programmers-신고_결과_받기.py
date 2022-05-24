def solution(id_list, report, k):
    result = [0] * len(id_list)
    rep_dic = {}
    
    for r in report:
        f, t = r.split()
        if t in rep_dic:
            rep_dic[t].add(f)
        else:
            rep_dic[t]={f}
    
    for key, value in rep_dic.items():
        if len(value) >= k:
            for user in value:
                result[id_list.index(user)]+=1
    
    return result