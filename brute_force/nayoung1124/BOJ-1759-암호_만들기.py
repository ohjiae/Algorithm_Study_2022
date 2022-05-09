from itertools import combinations, permutations
N,M = map(int, input().split())
alpha = list(input().split())
alpha.sort()
mini = []
ans = []


capable = list(combinations(alpha,N))
for capa in capable:
    cnt=0
    for i in capa:
        if i in ['a', 'e', 'i', 'o', 'u']:
            cnt+=1
    if cnt>=1 and N-cnt>=2:
        ans.append(capa)
for a in ans:
    print(''.join(a))
