def solution(n):
    global targetX, targetY
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    # 0,0 에서 초기화
    value = n ** 2
    direction = 0
    x, y = 0, 0
    matrix[x][y] = value
    value -= 1

    while value > 0:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if (0 <= nx < n) and (0 <= ny < n) and matrix[nx][ny] == 0:
            matrix[nx][ny] = value
            if value == target:
                targetX, targetY = nx, ny
            x, y = nx, ny
            value -= 1
        else:
            direction = (direction + 1) % 4
    return matrix


if __name__ == "__main__":
    n = int(input())
    target = int(input())
    targetX, targetY = 0, 0
    matrix = solution(n)
    for i in matrix:
        print(*i)
    print(targetX+1, targetY+1)
