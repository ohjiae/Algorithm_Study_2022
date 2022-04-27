n=int(input())
visit1=[False]*n # 세로
visit2=[False]*(2*n) #왼쪽 아래에서 오른쪽 위
visit3=[False]*(2*n) #왼쪽 위에서 오른쪽 아래
cnt=0
 
def queen(cur):
    global cnt
    if cur==n:
        cnt+=1
        return
    for i in range(n):
        if not visit1[i] and not visit2[cur+i] and not visit3[cur-i+n-1]:
            visit1[i]=True
            visit2[cur+i]=True
            visit3[cur-i+n-1]=True
            queen(cur+1)
            visit1[i]=False
            visit2[cur+i]=False
            visit3[cur-i+n-1]=False
 
 
queen(0)
print(cnt)