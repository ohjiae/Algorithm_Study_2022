N = int(input())
target = int(input())
targetX, targetY = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
matrix = [[0 for _ in range(N)] for _ in range(N)]
value = (N ** 2)
direction = 0
x, y = 0, 0

matrix[x][y] = value
value -= 1

while value > 0:
    nx = x + dx[direction]
    ny = y + dy[direction]

    if N <= nx < 0 and N <= ny < 0 and matrix[nx][ny] == 0:
        matrix[nx][ny] = value
        if value == target:
            targetX, targetY = nx, ny
        x, y = nx, ny
        value -= 1
    else:
        direction = (direction + 1) % 4

for row in matrix:
    print(*row)

print(targetX + 1, targetY + 1)
