n = int(input())
idx = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def out_of_bound(x, y):
    if x < 0 or y < 0 or x >= n or y >= n: return True
    return False

def find_idx(tar, arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == tar:
                return (i + 1, j + 1)

def printf(arr):
    for row in arr:
        for x in row:
            print(x, end=' ')
        print('')

def make_array(n):
    res = [[0] * n for _ in range(n) ]

    x, y = int(n/2), int(n/2)
    val = 1
    dist = 0
    dir = 0
    res[x][y] = val

    while True:
        if dir == 0 or dir == 2: dist += 1

        for _ in range(dist):
            val += 1
            x += dx[dir]
            y += dy[dir]
            if not out_of_bound(x, y):
                res[x][y] = val

        if val > n*n: break
        dir = (dir + 1) % 4
    return res

res = make_array(n)
x, y = find_idx(idx, res)
printf(res)
print(x, y)
