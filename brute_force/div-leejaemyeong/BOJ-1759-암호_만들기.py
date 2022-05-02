from itertools import combinations

L,C=map(int, input().split())
alpha=list(input().split())
alpha.sort()
vowels=['a','e','i','o','u']

for password in combinations(alpha,L):
    cnt=0
    for vowel in vowels:
        if vowel in password:
            cnt+=1
    if cnt==0 or cnt>L-2:
        continue
    else:
        print(''.join(password))