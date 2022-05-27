# 1. Heap 
## ✅ 자료구조
### **heap(힙)** 이란? 

- **최대값 / 최소값을 빠르게 찾아내기에 유리한,** 완전이진트리를 기본으로 한 자료구조
> **시간복잡도 비교** <br>
- 배열의 최대값, 최소값 찾기 = O(n) <br>
- Heap에서 찾기 = O(logn) 


- 다음과 같은 **부모와 자식 간**의 힙 속성을 만족함 (형제 사이에는 해당 X)
	- 항상 부모가 자식보다 값이 크거나(최대 힙) / 항상 부모가 자식보다 값이 작음 (최소 힙)
    
- 자식 노드의 최대 개수는 힙의 종류마다 다름, 보통 대부분의 경우 자식 노드의 개수가 최대 2개인 **이진 힙(Binary Heap)**을 사용
- 힙 정렬 뿐만 아니라 우선순위 큐, 허프만 코드를 구현할 때도 쓰임

<br>


## ✅ 종류 
![최대힙과최소힙](https://velog.velcdn.com/images/ohjiae/post/8fdaeaf0-d528-41c7-b0fd-53ff5441f7d4/image.png)
### 1) 최대 힙 (Max-Heap)

- 항상 부모노드 값이 자식노드의 값보다 크거나 같다.
그림의 왼쪽과 같이, 부모들이 항상 더 큰 값을 가지므로 제일 위의 root 노드가 **가장 큰 값**을 갖게 된다. 

### 2) 최소 힙 (Min-Heap)

- 항상 부모노드 값이 자식노드의 값보다 작다.
그림의 오른쪽과 같이, 부모들이 항상 더 작은 값을 가지므로, 제일 위의 root 노드가 **가장 작은 값**을 갖게 된다.

<br>

---
<p>

  
# 2. Heap Sort(힙 정렬)
  
  ## ✅ 과정
  ### 1-1. 데이터 삽입 (예시 : 최대 힙)
  1) 제일 아래 왼쪽 노드부터 채워짐
  2) 채워진 노드가 그 위치의 부모 노드보다 크면 부모 노드와 자리 바꿈
  
  ### 1-2. 데이터 삭제
  1) 보통 root 노드부터 삭제
  	- 최대값, 최소값을 사용하기 위해 사용하는 자료구조다 보니)
  2) root 노드 삭제 후, **가장 마지막에 추가한 노드**를 root 노드 자리로 옮김
  3) 새로운 root 노드가 아래의 자식 노드들보다 작으면, 자식 노드 중 큰 값의 노드와 자리를 바꿔줌
  

  ## ✅ 구현

  - 일반적으로 배열로 구현
  - 구현을 쉽게 하기 위해 루트 인덱스는 1이다.
  - 왼쪽 자식 인덱스 = 부모 인덱스 * 2
  - 오른쪽 자식 인덱스 = (부모 인덱스 * 2) + 1
  - 부모 인덱스 = 자식 인덱스 / 2
  - 위의 인덱스가 왜 저렇게 계산이 되는지 더 자세한 설명이 필요하다면? 
  [> 관련 블로그 링크 연결 (하단 그림 출처)](https://zeddios.tistory.com/56)
  ![트리와 배열의 인덱스 순서](https://velog.velcdn.com/images/ohjiae/post/046ab64a-2dde-4214-9f97-03bd9cf7c37e/image.png)
  - 트리와 배열의 인덱스 순서를 알 수 있는 그림 (빨간숫자가 인덱스)
	
  ### ⌨️ 코드
 	 
  

<br>

---  



---

<p>

# 3. 번외 : 힙(Heap)과 이진탐색트리(BST)의 공통점과 차이점
![힙과이진탐색트리](https://velog.velcdn.com/images/ohjiae/post/17941a5c-81b5-4e3c-bf8d-896cd5f52cff/image.png)
  
## ✅ 공통점 
  1. 둘 다 이진트리
## ✅ 차이점 
  1. **힙** : **최대값/최소값 검색** 을 위한 구조
  	- 각 부모 노드가 자식 노드보다 크거나 같음(최대 힙)/ 작거나 같음(최소 힙)
  	-  형제끼리는 조건이 없음 (왼쪽 자식 노드가 클 수도, 오른쪽 자식 노드가 클 수도 있음)
  <br>
  2. **이진 탐색 트리** : **탐색** 을 위한 구조
  	- 왼쪽 자식 노드 < 부모 노드 < 오른쪽 자식 노드 값 순으로 큼.
  <br>
  
  
<p>
  <br>
  <br>


> - 참고 사이트 및 자료 출처 
[LearnersBucket](https://learnersbucket.com/tutorials/array/heap-data-structure-in-javascript/)
[힙 (자료 구조) - 위키 백과](https://ko.wikipedia.org/wiki/%ED%9E%99_(%EC%9E%90%EB%A3%8C_%EA%B5%AC%EC%A1%B0))
[[DataStructure>Tree] Heap - Jay님 블로그](https://medium.com/@jyw198908/heap-45bbad579e0c)
[힙(Heap) 이란? - 오늘의코드 블로그](https://todaycode.tistory.com/56)
[Heap Sort 정렬 알고리즘 - Zeddios님 블로그](https://zeddios.tistory.com/56)
[Why is Binary Heap Preferred over BST for Priority Queue? - GeeksforGeeks](https://www.geeksforgeeks.org/why-is-binary-heap-preferred-over-bst-for-priority-queue/)
