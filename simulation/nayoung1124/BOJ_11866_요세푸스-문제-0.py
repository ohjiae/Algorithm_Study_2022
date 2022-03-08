from collections import deque
if __name__ == '__main__':
    N,M = map(int, input().split()) # 사람 수
    arr = [i for i in range(1, N + 1)]

    answer = []
    traget = 0

    for _ in range(N):
        traget += M - 1
        if traget >= len(arr):  # 한바퀴를 다 돌았을때 나머지로 바꿈
            traget = traget % len(arr)
        answer.append(str(arr.pop(traget)))
    print("<", ", ".join(answer), ">", sep='')
