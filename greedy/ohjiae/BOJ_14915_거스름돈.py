N=int(input())
def cal(N):
    if N%5==0: print(N//5)
    elif N<10:
        if N==1 or N==3: print(-1)
        elif N%2==0: print(N//2)
        else: print(cal(N-1)-1)
if N>=10 : cal(N)
elif (N%5)%2==0: print(N//5)+(N%5)//2
else: print(N//5)+((N%5)//2)+2
