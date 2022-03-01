n = int(input())
nums = [int(input()) for _ in range(n)]
result = 0
high = 0

for i in range(n-1, -1, -1):
    if nums[i] > high:
        result+=1
        high=nums[i]

print(result)