k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input().strip()))

low, high = 1, max(arr)
res = 0

def cut(mid):
    res = 0
    for e in arr:
        res += (e // mid)
    return res

while low <= high:
    mid = int((low + high)/2)
    tmp = cut(mid)

    if tmp >= n:
        low = mid + 1
        res = max(res, mid)
    else:
        high = mid - 1
print(res)