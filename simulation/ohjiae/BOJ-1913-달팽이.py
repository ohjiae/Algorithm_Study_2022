num = int(input())
find = int(input())
dic = {}
graph = [[0 for _ in range(num)] for _ in range(num)]
a = 0
for n in range(num,1,-2):
    for i in range(n-1):
        l = (n**2)-i
        dic[l]=[i+a,a]
        graph[i+a][a] = l

        d = (n**2)-n+1-i
        dic[d]=[num-a-1,i+a]
        graph[num-a-1][i+a] = d

        u = ((n-2)**2)+1+i
        graph[a][a+i+1] = u
        dic[u]=[a+1,a+i+2]

        r = ((n-2)**2)+n+i
        graph[i+1+a][num-a-1] = r
        dic[r]=[i+2+a,num-a]
    a += 1
graph[num//2][num//2] = 1

for i in range(num):
    print(*graph[i],sep= ' ')
print(*dic[find],end= ' ')