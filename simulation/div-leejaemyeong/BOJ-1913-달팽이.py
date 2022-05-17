N=int(input())
n=int(input())

arr=[[0 for _ in range(N)] for _ in range(N)]
num=1
dir=1
ch_dir=True
x=N//2
y=N//2
arr[x][y]=num
n_dir=[x,y]
while True:
    for i in range(dir):
        num += 1
        if num>(N*N): break
        if ch_dir:
            x-=1
        else:
            x+=1
        arr[x][y]=num
        if num==n:
            n_dir=[x,y]

    if num>(N*N):
        break

    for i in range(dir):
        num+=1
        if ch_dir:
            y+=1
        else:
            y-=1
        arr[x][y]=num
        if num==n:
            n_dir=[x,y]
    dir+=1
    if ch_dir:
        ch_dir=False
    else:
        ch_dir=True

for i in arr:
    print(' '.join(str(j) for j in i))
print(' '.join(str(i+1) for i in n_dir))



