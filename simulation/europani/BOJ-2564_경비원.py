def position(dir, dis):
    if dir == 1:
        x, y = 0, dis
    elif dir == 2:
        x, y = b, dis
    elif dir == 3:
        x, y = dis, 0
    else:
        x, y = dis, a
    return x, y

a, b = map(int, input().split())
n = int(input())
stores = []
result = 0

for _ in range(n):
    dir, dis = map(int, input().split())
    stores.append((position(dir, dis)))

dir, dis = map(int, input().split())
x, y = position(dir, dis)

# distance
for store_x, store_y in stores:
    # 맞은편일때
    if abs(store_x-x) == b:
        tmp = min(b+store_y+y, b+(a-store_y)+(a-y))
    elif abs(store_y-y) == a:
        tmp = min(a+store_x+x, a+(b-store_x)+(b-x))
    # 그외
    else:
        tmp = abs(store_x-x)+abs(store_y-y)
    result+=tmp
print(result) 