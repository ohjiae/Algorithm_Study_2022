k,n=map(int,input().split())
arr=[]
for _ in range(k):
    arr.append(int(input()))
 
start=1
end=sum(arr)//n
 
while start<=end:
    mid=(start+end)//2
    cnt=0
    for i in arr:
        cnt+=i//mid
    if cnt<n:
        end=mid-1
    else:
        start=mid+1
        ans=mid
 
print(ans)