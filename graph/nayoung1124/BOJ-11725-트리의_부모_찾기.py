import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
parentes = [0 for _  in range (N+1)]
tree = defaultdict(list)
for _ in range (N-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(start, tree, parents):
    for i in tree[start]:
        if parents[i]==0:
            parents[i]=start
            DFS(i,tree,parents)

DFS(1,tree,parentes)

for i in range(2,N+1):
    print(parentes[i])
