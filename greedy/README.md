 # **Greedy**

: 현재상황에서 당장 좋은 것만 고르는 알고리즘 설계 기법


## **개요**

* 최적해를 구하는데 주로 사용되는 근시안적인 방법이다.
* 최적화 문제란 가능한 해들 중에서 가장 좋은(최대, 최소)해를 찾는 문제이다.
* 여러 경우를 선택할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식이다.
* 한번 선택한 것은 번복하지 않아서 단순하거나 제한적인 문제들에 적용된다.
* 반드시 최적해를 구한다는 보장은 없다.


## **특징**


* 현재의 선택이 나중에 미칠영향은 고려하지 않는다.
* 외우지 않아도 풀 수 있는 알고리즘이다.
* '창의력' 이 필요하다.


## **조건**


* 항상 최적해로 갈 수 있음을 증명하면 항상 안전한 선택이 된다.
* 후의 경우가 상위 배수의 전제를 갖고있어야 한다.(예 : 거스름돈 문제)


## **어떤 상황에서 사용하는가?**
* 단순히 현재상황에서 가장 좋은 것을 선택해도 풀 수 있는 문제
* 문제풀이를 위한 아이디어를 떠올리고, 이것이 정당한지 검토할 수 있어야한다.
* 바로 문제 유형을 파악하기 어려운 문제

</br>

 ## BOJ-14916-거스름돈
```python
import sys
n = int(sys.stdin.readline())

cnt = 0
while True:
    if n % 5 == 0:
        cnt += (n // 5)
        print(cnt)
        break
    else:
        n -= 2
        cnt += 1

    if n < 0:
        print(-1)
        break
```

## BOJ-1931-회의실 배정
```python
import sys

n = int(sys.stdin.readline().rstrip())

time = []

for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time.append((s, e))

time.sort()                     #시작시간 기준 오름차순 정렬
time.sort(key=lambda x:x[1])    #종료시각(e) 기준 오름차순 정렬
# print(time)

room = 1
end_time = time[0][1]           #첫번째 회의의 끝나는 시각
#print(end_time)

for i in range(1, n):               # ex. 1번째 회의의 끝나는 시각과 2번째 회의의 시작하는 시각을 비교 2번째 회의의 시작 시각이 더 크다면
    if time[i][0] >= end_time:
        room += 1                   #사용할 수 있는 회의로 판단, room 을 +1해줌
        end_time = time[i][1]       #ex.end_time을 1번째 회의의 끝나는 시각에서 2번째 회의의 끝난는 시각으로 바꿔줌
print(room)
```

## BOJ-1202-보석도둑
```python
```