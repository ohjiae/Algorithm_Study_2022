n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(input()))

ans=n*n

for bit in range(1<<n):
    tmp=[arr[i][:] for i in range(n)]
    for i in range(n):
        if bit & (1<<i):
            for j in range(n):
                if tmp[i][j]=='T':
                    tmp[i][j]='H'
                else:
                    tmp[i][j]='T'
    cnt=0
    for i in range(n):
        cnt_t=0
        for j in range(n):
            if tmp[j][i]=='T':
                cnt_t+=1
        cnt+=min(cnt_t,n-cnt_t)
    ans=min(cnt,ans)

print(ans)