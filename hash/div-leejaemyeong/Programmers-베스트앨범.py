def solution(genres, plays):
    answer = []
    hash={}
    plays_sum={}
    for i in range(len(plays)):
        if genres[i] in hash:
            hash[genres[i]].append((plays[i],i))
            plays_sum[genres[i]]+=plays[i]
        else:
            hash[genres[i]]=[(plays[i],i)]
            plays_sum[genres[i]]=plays[i]
            
    hash_sort=dict(sorted(plays_sum.items(), key=lambda x:-x[1]))
    
    for key in hash_sort.keys():
        hash_value=sorted(hash[key], key=lambda x:(-x[0],x[1]))
        if len(hash_value) == 1:
            answer.append(hash_value[0][1])
        else:
            answer.append(hash_value[0][1])
            answer.append(hash_value[1][1])
            
    return answer