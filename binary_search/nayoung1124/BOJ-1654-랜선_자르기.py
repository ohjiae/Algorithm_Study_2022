import sys
K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
start, end = 1, max(lan) 

while start <= end:
    mid = (start + end) // 2 #중간 위치
    lines = 0 #랜선 수
    for i in lan:
        lines += i // mid #분할 된 랜선 수
        
    if lines >= N: #랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)
