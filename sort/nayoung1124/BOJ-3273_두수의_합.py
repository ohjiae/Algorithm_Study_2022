from collections import deque

n = int(input())
nums = list(map(int,input().split()))
target = int(input())
ans = 0
nums.sort()

left = 0
right = n-1

while left<right:
    tmp = nums[left]+nums[right]
    if tmp>target:
        right -=1
    elif tmp<target:
        left+=1
    else:
        ans+=1
        left+=1
        right-=1
print(ans)
