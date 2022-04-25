
# 이진탐색(binary search)
- 시간복잡도 : O(log N)
- 정렬된 자료를 반으로 나누어 탐색하는 방법
- 리스트를 항상 오름차순으로 정렬 후 사용가능

   ## 구현하기 위해 필요한 인자
   
   - target : 찾고자 하는 값
   - data : 오름차순으로 정렬된 list
   - start : data의 처음 값 인덱스(값)
   - end : data의 마지막 값 인덱스(값)
   - mid : start, end의 중간 인덱스(값)

   ## 구현 개요
   - 자료의 중간 값이 찾고자하는 값인지 검사
   - 찾고자하는 값이 아니면 start 또는 end값 이동
   - 동일 연산 반복

   - 예시
![image](https://velog.velcdn.com/images%2Fmadfinger%2Fpost%2F45278832-fcc8-4575-bb9c-955c352ba3e7%2Fimage.png)

   ## 바이너리 서치 구현
   ```
   def binary_search(target, data):
    data.sort()
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None
   ```

   - 재귀적 구현
   ```
   def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1        

    return binary_search_recursion(target, start, end, data)
   ```
