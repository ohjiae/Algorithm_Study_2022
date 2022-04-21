import sys
input = sys.stdin.readline
N,M = map(int,input().split())
tree = sorted(list(map(int,input().split())),reverse=True)
H = tree[0]-M
#기준 미달 다빼고 시작
for i in range(N):
    if tree[i]<=H:
        tree = tree[:i]
        break
#반으로 나누면서 적정지점 서치
tree.reverse()
start, end = tree[-1],tree[0]
while start<=end:
    mid = (start+end)//2
    gain = 0
    for i in tree:
        if i>= mid:
            gain += i-mid
    if gain >= M:
        start = mid + 1
    else:
        end = mid-1
print(end)
