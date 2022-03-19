# 시간 초과
if __name__ == '__main__':
    N,M= map(int,(input().split()))
    jewel = []
    bag = []
    price = 0
    for _ in range(N):
        jewel.append(list(map(int,(input().split())))) #[무게, 가격]
    for _ in range(M):
        bag.append(int(input()))
    jewel.sort(key=lambda x:(x[1],x[0]), reverse=True)
    bag.sort()
    for i in jewel:
        for idx,j in enumerate(bag):
            if i[0]<j:
                price += i[1]
                bag.pop(idx)
                break
            else: continue

    print(price)


