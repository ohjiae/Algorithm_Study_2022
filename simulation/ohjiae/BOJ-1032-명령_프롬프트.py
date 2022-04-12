words = [list(input()) for _ in range(int(input()))]
res = words[0]
for i in range(1,len(words)):
    for a in range(len(res)):
        if words[i][a] != res[a]:
            res[a] = '?'
print(''.join(res))
