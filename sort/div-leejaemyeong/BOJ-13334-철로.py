import heapq

n=int(input())
arr=[]
for _ in range(n):
    x=list(map(int,input().split()))
    arr.append(sorted(x))
arr.sort(key=lambda x:x[1])

d=int(input())
h_o=[]
for l in arr:
    x,y=l
    if (y-x)<=d:
        h_o.append(l)

heap=[]
cnt=0
for l in h_o:
    if not heap:
        heapq.heappush(heap,l)
    else:
        while heap[0][0] < l[1]-d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap,l)
    cnt=max(cnt,len(heap))

print(cnt)