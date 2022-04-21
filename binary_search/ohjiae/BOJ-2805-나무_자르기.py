import sys
input = sys.stdin.readline()
N,M = int(input().split())
tree = sorted(list(map(int,input().split())),reverse=True)
H = tree[0]-M
gain = 0

# for문 시작
# H만큼 자르면서 gain+
# gain 채워지면 break
# for문 끝
# gain이
for i in range(tree):
    gain += i-cut
    if gain >=
print(tree)
