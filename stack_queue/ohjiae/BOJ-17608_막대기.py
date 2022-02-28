'''
# 접근 방법
입력을 다 받고, 마지막으로 받은 막대가 시야의 기준이 되므로 '스택' 구조를 사용한다.
(앞에서 세면 뒤쪽에 가리는 것을 찾고 그전의 것을 지우는 과정을 반복해야해서 비효율적)

- max 이전의 막대는 어차피 안보이므로, max에 도달하면 멈춘다.
- 세는동안 기준보다 작은 막대는 넣지 않는다.
- 기준보다 클 경우에만 넣고 그걸 새로운 기준으로 만든다. 
'''

#from sys import stdin
#input = stdin.readline
def stack():
    stk = [int(input()) for _ in range(int(input()))]
    longest = max(stk)
    visible = 0 # 보이는 개수 세기
    stlen = 0 # 기준이되는 막대 길이
    while stk:
        s = stk.pop() 
        if s == longest:
            visible += 1
            break
        elif s > stlen: # 기준 막대보다 길면
            stlen = s # 새 기준 세우고
            visible += 1 # 개수 셈
    return print(visible)

stack()

