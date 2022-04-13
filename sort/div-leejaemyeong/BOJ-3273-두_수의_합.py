n=int(input())
arr=list(map(int,input().split()))
x=int(input())
cnt=0
arr.sort()
left=0
right=n-1
while left<right:
    temp=arr[left]+arr[right]
    if temp == x:
        cnt+=1
        left+=1
    elif temp < x:
        left+=1
    else:
        right-=1
print(cnt)