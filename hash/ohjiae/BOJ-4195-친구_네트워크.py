for t in range(int(input())):
    sets = []
    for j in range(int(input())):
        s_list = []
        a, b = map(str,input().split())
        print('HIHIHI',sets,'slist',s_list)
        for i in range(len(sets)): # 포함되는 친구셋 찾고 인덱스 따로저장
            if a in sets[i] or b in sets[i]:
                sets[i].update([a,b])
                s_list.append(i)
                print(f'i={i},s_list={s_list},sets[i]={sets[i]},\n,{sets}')
                if len(s_list) > 1:
                    break #2개가 최대이므로 찾은게 2번째면 멈춤

        if len(s_list) == 0 : # 포함되는 set 없을때 추가
            sets.append(set([a,b]))
            s_list.append(0)
            print(2)
        elif len(s_list) == 1: #하나에 포함되면 set 길이 출력
            print(len(sets[0]))
        else: # a,b 포함 set이 2개일 때 두 set을 합치고 그 길이 출력
            tmp = set()
            for s in range(len(s_list),0,-1):
                idx = s_list[s]
                tmp.update(sets.pop(idx))
                print('hereee!@!@',s_list,idx,sets,'\n','tmp=',tmp)
            sets.append(tmp)
            print(len(tmp))