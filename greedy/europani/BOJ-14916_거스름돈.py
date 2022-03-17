n = int(input())
result = 0

while n>0:
    if n%5==0:
        result+=n//5
        n%=5
    else:
        n-=2
        result+=1

print(result if n>=0 else -1)