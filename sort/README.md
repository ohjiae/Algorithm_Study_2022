# Algorithm_Study_2022

## 정렬(Sort)
- 데이터를 특정 기준에 따라 순서대로 나열하는 것
- 일반적으로 문제 상황에 따라 적절한 정렬 알고리즘이 공식처럼 정해짐
<br>

### 1. 선택정렬
- 한바퀴 돌 때 가장 작은 값을 찾아 맨 앞과 교환하는 방식의 정렬
- 맨 앞에서부터 정렬한다는 특징
- 최악의 성능 O(n^2)
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] 

for i in range(len(array)): 
  min_index = i
  for j in range(i+1, len(array)): 
    if array[j] < array[min_index]: 
      min_index = j # 처리되지 않은 데이터 중에서 가장 작은 데이터를 찾는다 
      array[i], array[min_index] = array[min_index], array[i] # SWAP 스와핑
      
print(array)
```
<br>

### 2. 삽입정렬
- 정렬된 데이터 그룹을 늘려가며 추가되는 데이터는 알맞은 자리에 삽입하는 방식
- 구현은 간단
- 최악의 성능 O(n^2)
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] 
for i in range(1, len(array)): 
  for j in range(i, 0, -1): # 인덱스 i부터 1씩 감소하며
    if array[j] < array[j-1]: 
      array[j], array[j-1] = array[j-1], array[j] 
      else: # 자신보다 적은 데이터를 만나면 그 위치에서 멈춘다 
        break 
print(array)
```
<br>

### 3. 버블정렬
- 인접한 두 수를 비교하며 정렬해나가는 방식
- 앞에서부터 시작하여 큰 수를 뒤로 보내 뒤가 가장 큰 값을 가지도록 완성해나가는 방법 
- 최악의 성능 O(n^2)
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1,len(array)):
  for j in range(0,len(array)-1):
    if array[j] > array[j+1]:
          array[j], array[j + 1] = array[j + 1], array[j]
print(array)
```
<br>

### 4. 병합정렬
- 분할 정복과 재귀를 이용한 알고리즘으로 O(n log n)의 시간 복잡도
- 반으로 쪼개고 다시 합치는 과정에서 그룹을 만들어 정렬하게 되며 이 과정에서 2n 개의 메모리가 소요
- 배열을 더이상 나눌수 없을때(len(arrat)==1)까지 나누고, 병합하면서 정렬
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr
    
print(merge_sort(array))
```

```
[7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
[7, 5, 9, 0, 3][1, 6, 2, 4, 8]
[7, 5][9, 0, 3][1, 6][2, 4, 8]
[7, 5][9, 0] [3][1, 6][2, 4][8]
[7][5][9][0][3][1][6][2][4][8]
[5, 7][0, 9][1, 3][2, 6][4, 8]
[0, 5, 7, 9][1, 2, 3, 4, 6, 8]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<br>

### 5. Quick sort
-병합 정렬과 마찬가지로 분할 정복 알고리즘으로 평균적으로 빠른 속도
- 추가적인 메모리가 공간이 필요 없다
- 병합 정렬은 균등하게 분할하였다면 퀵 정렬은 Pivot을 설정하고 그 기준으로 정렬
```python
def quick_sort(array):
	if len(array) <= 1:
		return array
	pivot = len(array) // 2
	front_arr, pivot_arr, back_arr = [], [], []
	for value in array:
		if value < array[pivot]:
			front_arr.append(value)
		elif value > array[pivot]:
			back_arr.append(value)
		else:
			pivot_arr.append(value)
	print(front_arr, pivot_arr, back_arr)
	return quick_sort(front_arr) + quick_sort(pivot_arr) + quick_sort(back_arr)
  
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]  
print(quick_sort(array)
```
<br>

### 6. 계수정렬
- 모든 데이터가 양의 정수인 상황에서 데이터의 개수를 N, 데이터 중 최대값의 크기를 K라고 할 때, 
- 계수 정렬의 시간 복잡도는 O(N + K)이다
- 따라서 데이터의 범위만 한정되어 있다면 효과적으로 사용할 수 있으며 항상 빠르게 동작한다.
- 계수 정렬은 정렬하고자 하는 배열의 최대값이 매우 클 때 메모리를 매우 비효율적으로 쓰게 된다는 단점이 있다.
- count 배열의 인덱스를 통해서 숫자의 개수를 세어주는 방식이기 때문에, 만약 배열에 음수가 존재한다면 사용할 수 없다.
```python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
count = [0] * (max(array) + 1)

for num in array:
    count[num] += 1
    
for i in range(1, len(count)):
    count[i] += count[i-1]

result = [0] * (len(array))

for num in array:
    idx = count[num]
    result[idx - 1] = num
    count[num] -= 1

print(result)
```
<br>

### Python에서의 정렬
'''python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] 
result = sorted(array) 
print(result)
'''
- sorted는 병합 정렬을 기반으로 한다. 
- 퀵 정렬보다 느리지만 최악의 경우에도 시간 복잡도O(NlogN)을 보장한다는 특징이 있다
- 집합 자료형이나 딕셔너리 자료형을 입력받아도 반환되는 결과는 리스트 자료형이다

'''python
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8] 
array.sort()
print(result)
'''
- 리스트 변수가 하나 있을 때 내부 원소를 바로 정렬할 수도 있다
- 리스트 객체의 내장 함수인 sort()
- 이때는 별도의 정렬된 리스트를 반환하지 않고 내부 원소가 바로 정렬

<br>

### 코딩테스트
문제에서 별도의 요구가 없다면 기본 정렬 라이브러리를 사용하고, 데이터의 범위가 한정되어 있으며 더 빠르게 동작해야 할 때는 계수 정렬을 사용하자

- 정렬 라이브러리로 풀 수 있는 문제: 단순히 정렬 기법을 알고 있는지 물어보는 문제
- 정렬 알고리즘의 원리에 대해서 물어보는 문제: 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 알고 있어야 문제를 풀 수 있다.
- 더 빠르 정렬이 필요한 문제: 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진 알고리즘의 구조적인 개선을 거쳐야 풀 수 있다

