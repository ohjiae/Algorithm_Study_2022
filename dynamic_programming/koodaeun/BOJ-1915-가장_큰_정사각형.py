# 첫째 줄에 n, m이 주어진다. 다음 n개의 줄에는 m개의 숫자의 배열로 주어진다.
# 이 배열에서 1로 된 가장 큰 정사각형의 넓이를 출력한다.

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