def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        str=''
        for x in tree:
            if x in skill:
                str+=x
            
        # verify
        if str==skill[:len(str)]:
            answer+=1
    
    return answer