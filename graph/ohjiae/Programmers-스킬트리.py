def solution(skill, skill_trees):
    answer = 0
    leng = len(skill)
    while skill_trees:
        done = [False for _ in range(leng)]
        flag = True
        cur_sk = skill_trees.pop()
        for s in cur_sk: #배운 스킬이
            if s in skill: #기준 스킬트리에 포함되고
                idx = skill.index(s)
                if idx == 0: #첫스킬일 때
                    if idx != 0: # 기준스킬의 첫번째글자가 아닐 때
                        flag = False
                        break
                    else :
                        done[idx] = True #첫번째면 배움처리

                elif not done[idx-1]: #전스킬 안배운경우
                    flag = False # 틀림 처리
                    break
                else : #배웠으면
                    done[idx] = True #이번스킬 배움 처리
        if flag: answer += 1
    return answer

# print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))


def solution(skill, skill_trees):
    answer = 0
    for skills in skill_trees:
        skill_order = list(skill)
        for s in skills:
            if s in skill_order and s != skill_order.pop(0): break
        else: answer += 1

        #   if s in skill_order and s == skill_order.pop(0): answer += 1
        # else : break >> 이 주석라인은 틀림
    return answer