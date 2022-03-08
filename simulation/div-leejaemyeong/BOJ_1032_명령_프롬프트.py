n=int(input())
s=input()
arr=[True]*(len(s)+1)
for _ in range(n-1):
    s1=input()
    for i in range(len(s)):
        if s1[i]!=s[i]:
            arr[i]=False
arr1=[]
for i in range(len(s)):
    if arr[i]:
        arr1.append(s[i])
    else:
        arr1.append('?')
print(''.join(i for i in arr1))
