n = int(input())
nums = sorted(map(int, input().split()))
t = int(input())
result = 0

left=0
right=n-1

while left < right:
    if nums[left]+nums[right] == t:
        result+=1
        left+=1
        right-=1
    elif nums[left]+nums[right] > t:
        right-=1
    else:
        left+=1

print(result)