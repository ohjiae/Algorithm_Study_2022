N = int(input())
if N%5==0: print(N//5)
elif N<5: print(N//2 if N%2 == 0 else -1)
else:
    M = N % ((N//5)*5)
    P = [2, 1, 3, 2]
    for i in range(1, 5):
        if i==M:
            print((N//5)+P[i-1])
