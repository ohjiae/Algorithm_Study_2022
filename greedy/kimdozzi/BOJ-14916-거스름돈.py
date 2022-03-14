n = int(input())
total = 0
while n > 0:
    if n % 5 == 0 :
        total += (n // 5)
        break
    n -= 2
    total += 1

if n < 0 :
    print(-1)
else:
    print(total)


