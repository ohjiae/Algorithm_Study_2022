n = int(input())
cord = []
for i in range(n):
    cord.append(list(map(int, input().split())))

if __name__ == "__main__":
    # n : 전깃줄 갯수, cord : 전깃줄이 연결된 idx
    # lis : 현재 idx까지 lis 길이
    # lis를 위해 asc 정렬
    cord.sort()
    lis=[1] * n
    for i in range(n):
        for j in range(i):
            if cord[j][1] < cord[i][1]:
                lis[i] = max(lis[i], lis[j] + 1)
    # increasing order로 올바르게 연결된 전깃줄들은 교차점이 존재하지 않으므도
    # 전체 갯수에서 lis수만큼 제외
    print(n - max(lis))