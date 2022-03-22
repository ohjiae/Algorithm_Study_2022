n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time.sort(key=lambda x: (x[1], x[0]))

now = 0
result = 0

for start, end in time:
    if start > now:
        now=end
        result+=1

print(result)