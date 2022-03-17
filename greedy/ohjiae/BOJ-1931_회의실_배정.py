from sys import stdin
n = int(input())
schedules = [list(map(int, stdin.readline().split())) for _ in range(n)]
schedules.sort(key = lambda x : (x[1],x[0]))
end = 0 
cnt = 0
for s, e in schedules:
    if end <= s:
        cnt += 1
        end = e
print(cnt)
