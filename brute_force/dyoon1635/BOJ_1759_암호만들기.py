from itertools import combinations

l, c = map(int, input().split())
words = list(input().split())
res = set()

def check(pwd):
    vowel = ['a','e','i','o','u']
    wc1 = 0
    wc2 = 0
    for p in pwd:
        if p in vowel: wc1 += 1
        else: wc2 += 1
    if wc1 >= 1 and wc2 >= 2: return True
    return False


for pwd in combinations(words, l):
    if not check(pwd): continue

    pwd = sorted(pwd)
    tmp = ''
    for w in pwd: tmp += w
    res.add(tmp)
res = sorted(res)
for pwd in res: print(pwd)