def solution(genres, plays):
    answer = []
    gnr_p = {}  # {장르 : 총 재생수}
    songs = {}  # {장르 : [(재생1위 인덱스, 플레이 수), (재생2위 인덱스, 플레이 수)], ...}
    for i in range(len(genres)):
        n_gen = genres[i]
        n_ply = plays[i]
        fst, snd = 0, 1
        if n_gen in songs:  # 이미 있는 장르면 비교 시작
            gnr_p[n_gen] += n_ply
            if len(songs[n_gen]) == 2:  # 2곡일 때
                if n_ply > songs[n_gen][fst][1]:
                    tmp = songs[n_gen][fst]
                    songs[n_gen] = [(i, n_ply), tmp]
                elif songs[n_gen][fst][1] >= n_ply > songs[n_gen][snd][1]:
                    songs[n_gen][snd] = (i, n_ply)
            else:
                if n_ply > songs[n_gen][fst][1]:
                    tmp = songs[n_gen][fst]
                    songs[n_gen] = [(i, n_ply), tmp]
                else:
                    songs[n_gen].append((i, n_ply))
        else:  # 장르 첫 곡
            gnr_p[n_gen] = n_ply
            songs[n_gen] = [(i, n_ply)]

    # 총 플레이수로 장르 sorted 하고 인덱스 answer에 추가
    gnr_p = sorted(list(zip(gnr_p.values(), gnr_p.keys())), reverse=True)
    for gnr in gnr_p:
        for s in songs[gnr[1]]:
            answer.append(s[0])
    return answer