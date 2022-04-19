def solution(numbers):
    str_nums = []
    for k in numbers:
        str_nums.append(str(k))

    str_nums.sort(key = lambda x:x*5, reverse=True)
    
    if sum(numbers)==0:
        return '0'
    
    return ''.join(str_nums)
