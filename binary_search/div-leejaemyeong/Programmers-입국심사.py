def solution(n, times):
    answer = 0
    start=0
    end=max(times)*n
    while start<end:
        mid=(start+end)//2
        cnt=0
        for i in times:
            cnt+=mid//i
        if n<=cnt:
            end=mid
        else:
            start=mid+1
    answer=start
    return answer