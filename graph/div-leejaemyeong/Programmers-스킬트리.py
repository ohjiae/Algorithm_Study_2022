def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        num=0
        ch_order=True
        for i in skill:
            if i in tree:
                if num>tree.index(i) or not ch_order:
                    num=-1
                    break
                else:
                    num = tree.index(i)
            else:
                ch_order=False
        if num!=-1:
            answer+=1
            
    return answer
