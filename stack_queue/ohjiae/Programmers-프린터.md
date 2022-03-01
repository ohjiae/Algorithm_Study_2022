# '프로그래머스 - 프린터' 풀이 비교

## 1. 이번 풀이

### 1) 코드

```python
from collections import deque
def solution(priorities, location):
    answer = 0
    printlist = deque((n,p) for n,p in enumerate(priorities))

    maxpr = max(printlist, key = lambda x:x[1])

    while printlist:
        tmp = printlist.popleft()
        if tmp[1] < maxpr[1]:
            printlist.append(tmp)
        else :
            answer += 1
            if tmp[0] == location:
                break
            maxpr = max(printlist, key = lambda x:x[1])
    return answer
```

### 2) 결과

![스크린샷 2022-03-01 오후 5 19 08](https://user-images.githubusercontent.com/77822999/156133711-2924ba6b-a095-44b7-8fcf-b76593e39571.png)

## 2. 예전 풀이
> 지난 풀이가 더 간단하게 생겨서 뜯어보니, 다른건 다 비슷한데<br>
    튜플에서 max 계산시, 앞의 원소([0]번째)부터 계산하는걸 이용해<br>
    우선순위를 앞의원소로 바꿔서 배치해서 비교했더라구요.<br>
    근데 **의문점** 이 드는게, <br>
    while문 안의 if문 조건에서 제가 왜인지 모르게 q를 넣었는데,<br>
    q and 이조건을 빼주면 2,5,18번에서 런타임 에러가 납니다(아마 느려서 그런듯)<br>
    근데 엄청 예전에 푼건지 q and 이조건이 이해가 안되네요 ㅠㅠ <br>
    제가풀고 제가 이해가안되는게 참^^...


### 1) 코드

```python
def solution(priorities, location):
    from collections import deque
    q = deque([(p,i) for i,p in enumerate(priorities)])
    answer = 0

    while q:
        np = q.popleft()
        if q and max(q)[0] > np[0]:
            q.append(np)
        else :
            answer += 1
            if np[1] == location:
                break

    return answer
```

### 2) 결과

![스크린샷 2022-03-01 오후 5 19 39](https://user-images.githubusercontent.com/77822999/156133656-f44221fa-8b17-42a1-b0c5-9a049e6106eb.png)


## 2. 예전 풀이 보고 이번 풀이 수정

### 1) 코드

```python
from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque((n,p) for n,p in enumerate(priorities))

    while q:
        tmp = q.popleft()
        if tmp[1] < max(q, key=lambda x:x[1])[1]:
            q.append(tmp)
        else :
            answer += 1
            if tmp[0] == location:
                break
    return answer
```

### 2) 결과 : 
- 2,5,18 런타임에러 (느려서 그런듯)
