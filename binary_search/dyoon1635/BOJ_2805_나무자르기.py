n, m = map(int, input().split())
forest = list(map(int, input().split()))

low, high = 1, max(forest)
res = 0

def M(mid):
    res = 0
    for tree in forest:
        if tree > mid:
            res += (tree - mid)
    return res

while low <= high:
    mid = int((low + high)/2)
    tmp = M(mid)

    if tmp < m: high = mid - 1
    else:
        low = mid + 1
        res = max(res, mid)
print(res)