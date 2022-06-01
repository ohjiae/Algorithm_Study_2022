# Hash Table
## 해쉬 구조란?
- 키(key)와 값(value)쌍으로 이루어진 데이터 구조
- Key를 이용해 데이터를 찾으므로 속도를 빠르게 만드는 구조
- 파이썬에서는 딕셔너리타입이 해쉬 테이블과 같은 구조

## 장점
- 데이터 저장/검색 속도가 빠름
- 키에 대한 데이터가 있는지 확인이 쉬움

## 단점
- 일반적으로 저장공간이 많이 필요
- 여러 키에 해당하는 주소가 동일할 경우 충돌 발생

## 시간 복잡도
- 일반적인 경우(충돌이 없는 경우) : O(1)
- 최악의 경우(모든 경우 충돌이 발생하는 경우) : O(n)

## 용어
- 해쉬(Hash) : 임의 값을 고정 길이로 변환하는 것을 의미
- 해쉬 함수(Hash Function) : 특정 연산을 이용해 키 값을 받아서 value를 가진 공간의 주소로 바꾸는 함수
- 해쉬 테이블(Hash Table) : 해쉬 구조를 사용하는 데이터 구조
- 해쉬 값(Hash Value) : Key값을 해쉬 함수에 넣어서 얻은 주소값
- 슬롯(Slot) : 한 개의 데이터를 저장할 수 있는 공간



![해쉬](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FRf9ew%2FbtqBD2nxuS2%2FNcjU5klHVOqPfEm28syiFk%2Fimg.png)

---

## 구현
### hash table 만들기

[In] 
```python
hash_table=list([0 for i in range(5)])
print(hash_table)
```
[Out]
```python
[0, 0, 0, 0, 0]
```

### 해쉬 함수 만들기
Divison 방법
```python
#키에 대한 해쉬값 리턴
def hash_func(key):
	return key % 5
```

### 해쉬 테이블에 값 저장(data가 문자열인 경우)
```python
def storage_data(data, value):
	key = ord(data[0])
	hash_address = hash_func(key)
	hash_table[hash_address] = value
```
### 해쉬 테이블에서 특정 주소의 데이터를 가져오는 함수
```python
def get_data(data):
	key = ord(data[0]
	hash_address = hash_func(key)
	return hash_table[hash_address]
```

### 데이터 저장
[In]
```python
storage_data('Dave','1234')

print(get_data('Dave')
print(hash_table)
```
[Out]
```python
1234
[0, 0, 0, '1234', 0]
```
---

## 충돌 해결 알고리즘
### Chaining 기법
- 해쉬테이블 저장공간 외에 공간을 더 추가해서 사용하는 방법
- 충돌 발생시, 링크드 리스트로 데이터를 추가로 뒤에 연결시키는 방법



![Chaining기법](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcVfCu9%2FbtqCNHoMaih%2FfafR6GXkS0phqYu6jm40ak%2Fimg.png)



### Linear Probing 기법
- 해쉬 테이블 저장공간 안에서 충돌 문제를 해경하는 방법
- 충돌이 일어나면 해당 hash value의 다음 index부터 맨 처음 나오는 빈공간에 저장하는 기법



![Linear Probing기법](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FdnRJ8R%2FbtqCKzS0HBD%2F5jew4WeGcXRAaIx5eh4JZ0%2Fimg.png)



### 공간을 확장하는 방법
- 해쉬 테이블의 크기를 확장시키는 방법

---

> - 참고 사이트
[파이썬으로 구현하는 자료구조 요약 정리 - 해쉬 테이블(Hash Table)](https://davinci-ai.tistory.com/19)/
[대표적인 자료구조: 해쉬 테이블 - 잔재미코딩](https://www.fun-coding.org/Chapter09-hashtable.html)
