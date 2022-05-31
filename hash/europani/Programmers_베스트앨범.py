from collections import defaultdict

def solution(genres, plays):
    # make dict
    dic_song = defaultdict(list)
    dic_sum = defaultdict(int)
    for i in range(len(genres)):
        dic_song[genres[i]]+=[[i, plays[i]]]
        dic_sum[genres[i]]+=plays[i]

    
    # get result
    result = []
    for k, v in sorted(dic_sum.items(), key=lambda x: x[1], reverse=True):
        for i, v in sorted(dic_song[k], key=lambda x: x[1], reverse=True)[:2]:
            result.append(i)


    return result