n,m=map(int,input().split())
trees=list(map(int,input().split()))
 
start=0
end=max(trees)
 
def binary_search(target, start, end):
    while start<=end:
        mid=(start+end)//2
        l=cnt_tree(mid)
        if l>=target:
            start=mid+1
        else:
            end=mid-1
    return end
 
def cnt_tree(a):
    length=0
    for i in trees:
        if a<i:
            length+=i-a
    return length
 
print(binary_search(m,start,end))