n, m = map(int,input().split())

table = []
result = 0

for i in range (n):
    table.append(list(map(int, list(input().rstrip()))))

for i in range(n):
    for j in range(m):
        if i > 0 and j > 0 and table[i][j] == 1:
            table[i][j] += min(table[i][j-1], table[i-1][j], table[i-1][j-1])
        result = max(result, table[i][j])

print(result * result)
