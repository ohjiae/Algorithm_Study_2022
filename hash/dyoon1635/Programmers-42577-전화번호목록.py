def solution(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i].startswith(arr[i + 1]) or \
        arr[i + 1].startswith(arr[i]):
            return not True
    return not False    