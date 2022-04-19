n, k = map(int, input().split())
lines = [int(input()) for _ in range(n)]

left = 1
right = max(lines)
answer = 0

while left <= right:
    mid = (left+right)//2

    cnt=0
    for line in lines:
        cnt+=line//mid

    if cnt >= k:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1
print(answer)