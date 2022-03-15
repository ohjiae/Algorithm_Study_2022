if __name__ == "__main__":
    n = int(input())
    cnt = 0
    if n == 1 or n == 3:
        print(-1)
        exit(0)

    change = 5
    while n:
        if n < change:
            change = 2

        n -= change
        cnt += 1
        if n == 1:
            cnt += 2
            break
    print(cnt)