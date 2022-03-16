n=int(input())
cnt=0
cnt+=n//5
n=n%5
if n%2!=0 and cnt>0:
    n+=5
    cnt-=1
    cnt+=n//2
elif n%2==0: cnt+=n//2
else: cnt=-1
print(cnt)