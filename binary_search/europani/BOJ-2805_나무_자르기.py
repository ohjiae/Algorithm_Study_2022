n, t = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)
answer = -1

while left <= right:
    mid = (left+right)//2

    poket = sum(tree-mid for tree in trees if tree-mid>=0)

    if poket >= t:
        answer = mid
        left=mid+1
    else:
        right=mid-1
print(answer)