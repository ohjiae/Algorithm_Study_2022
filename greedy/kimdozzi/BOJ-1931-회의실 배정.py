import sys
N = int(input())
lst = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
sorted_lst = sorted(lst,key=lambda x : (x[1],x[0]))
total = []
total.append(sorted_lst[0])
for i in range(1,len(sorted_lst)) :
    if total[-1][1] > sorted_lst[i][0]:
        continue
    total.append(sorted_lst[i])
print(len(total))
