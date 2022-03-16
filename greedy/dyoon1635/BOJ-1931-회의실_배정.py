if __name__ == "__main__":
    n = int(input())
    office_time = []
    cnt = 0
    for _ in range(n):
        start, end = map(int, input().split())
        office_time.append((start, end))
    office_time.sort()
    office_time.sort(key=lambda x: x[1])

    flag = 0
    for start, end in office_time:
        if flag <= start:
           flag = end
           cnt += 1
    print(cnt)
