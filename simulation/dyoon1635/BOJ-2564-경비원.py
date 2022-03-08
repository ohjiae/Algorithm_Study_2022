def Hash(x, y, r, c):
    if x == 1:
        return y
    elif x == 2:
        return (2*r + c) - y
    elif x == 3:
        return (2*r + 2*c) - y
    elif x == 4:
        return r + y

def getDistance(my_pos, shop, r, c):
    res = 0
    road_length = 2*r + 2*c
    for i in range(len(shop)):
        tmp = abs(my_pos - shop[i])
        res += min(tmp, abs(tmp - road_length))
    return res

def main():
    shop = []
    r, c = map(int, input().split())
    n = int(input())
    for _ in range(n):
        x, y = map(int, input().split())
        shop.append(Hash(x, y, r, c))

    x, y = map(int, input().split())
    my_pos = Hash(x, y, r, c)
    res = getDistance(my_pos, shop, r, c)
    print(res)

if __name__ == "__main__":
    main()