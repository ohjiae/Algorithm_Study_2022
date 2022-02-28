'''
# 접근 방법
입력을 다 받고, 마지막으로 받은 막대가 시야의 기준이 되므로 '스택' 구조를 사용한다.
(앞에서 세다가 더 높은 막대가 와서 앞의 시간이 무용지물이 되는 일이 없도록, 
뒤에서부터 세는 스택을 사용하는 것.)

- max 이전의 막대는 어차피 안보이므로, max를 먼저 찾고 Range를 (맨끝,max)로 설정한다.
세는동안 기준보다 작은 막대는 뺀다.

# 생각할 수 있는 경우
- 제일 마지막 막대가 제일 긴 막대인 경우
- 10 2 2 2 5 6 4 
'''

#from sys import stdin
#input = stdin.readline
stk = [int(input()) for _ in range(int(input()))]

def cnt(li):
    longest = max(li)
    visible = 0 # 보이는 개수 세기
    N = list.pop() # 기준이 되는 마지막 막대
    
    if N != longest :
        while li: # 원소가 있는동안 실행
            st = list.pop()
            if st > N :
                visible += 1

    else : # 마지막 막대가 제일 길 때
        return(1)