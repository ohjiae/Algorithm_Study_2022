'''
n = int(input())
s = set(map(int,input().split()))
x = int(input())
cnt = 0
for i in s:
    if x-i in s:
        cnt += 1
print(cnt//2)
'''
n = int(input())
nums = list(map(int,input().split()))
x = int(input())
cnt = 0
s = set()
for i in nums:
    if i in s:
        cnt += 1
    elif i <= x:
        s.add(x-i)
print(cnt)
