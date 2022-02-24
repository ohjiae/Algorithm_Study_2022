import sys

def stars(n) :
    matrix = []
    for i in range(3 * len(n)) :
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)

    return (list(matrix))

star = ["***", "* *", "***"]
n = int(sys.stdin.readline())
k = 0
while n != 3 :
    n = int(n/3)
    k += 1

for i in range(k) :
    star = stars(star)

print(*star, sep='\n')