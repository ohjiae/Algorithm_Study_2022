def solution(numbers):
    strs = sorted((str(x) for x in numbers), key=lambda x:x*4, reverse=True)

    if sum(numbers) == 0:
        return '0'

    return ''.join(strs)