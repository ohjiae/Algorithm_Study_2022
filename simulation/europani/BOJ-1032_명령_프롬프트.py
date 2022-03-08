n = int(input())
cmd = list(input() for _ in range(n))
result = ''

for i in range(len(cmd[0])):
    for j in range(1, n):
        if cmd[j-1][i] != cmd[j][i]:
            result+='?'
            break
    else:
        result+=cmd[0][i]

print(result) 