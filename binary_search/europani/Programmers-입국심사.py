def solution(n, times):
    answer = 0
    
    left = min(times)
    right = n*max(times)//len(times)
    
    while left <= right:
        mid = (left+right)//2
        ppl = 0
        
        # mid초동안 ppl명 심사
        for time in times:
            ppl+=mid//time
        
        if ppl >= n:
            answer=mid
            right=mid-1
        else:
            left=mid+1
    
    return answer
    