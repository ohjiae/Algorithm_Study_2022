n = int(input())
target = int(input())
arr = [[0]*n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = n//2, n//2
target_xy = []

def snail(i, d):
    global x, y
    # init
    arr[x][y]=i
    r=1
  
    while True:
        for _ in range(2):
            for _ in range(r):
                if i==target:
                    target_xy.append(x+1)
                    target_xy.append(y+1)
                if i >= n**2:
                    return
                  
                i+=1
                x, y = x+dx[d%4], y+dy[d%4]
                arr[x][y]=i
            d+=1
        r+=1

snail(1, 0)
for x in arr:
    print(*x)
print(*target_xy)