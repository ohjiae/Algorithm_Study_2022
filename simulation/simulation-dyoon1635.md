Baekjoon 20055 컨베이어 벨트 위의 로봇
===============

<hr/>

link : https://www.acmicpc.net/problem/20055

<hr/>

##### **1. Problem & Algorithm**
> * ###### 단순 simulation
> * ###### 길이가 2n인 conveyor belt 위에 로봇을 올리고, 특정 조건을 만족할 때까지 계속 구동
> * ###### 문제 서술부에는 컨베이어 벨트가 1-base로 되어 있으나, 개발 편의를 위해 0-base로 코딩
> * ###### pop, append가 자주 일어나므로 속도적인 측면을 고려하여 deque 사용
> * ###### algorithm에만 집중하기 위해 variable은 global 선언

##### **2. variable & function**
> * variable
>    * n : belt의 한쪽 면의 size
>    * k : belt의 종료 조건 :: count(내구도==0) > k인 경우 프로그램 종료
>    * belt : belt의 각 위치의 내구도
>    * robot : belt위의 robot들이 어느 위치에 있는지를 저장 (asc로 정렬)
>    * step : belt가 총 몇 단계를 수행했는지 count
> * function
>    * def count_zero()
>        * belt를 처음부터 끝까지 순회하며 값이 0인 부분의 갯수를 count
>        * default는 true return 갯수가 k이상이면 false return
>    * def step_1()
>        * belt가 시계 방향으로 한 칸 회전
>        * robot도 같이 회전. robot은 각자 위치한 belt의 idx만 가지고 있으므로 robot deque의 전체 값 +1 
>        * robot이 끝 점에 도달하면 belt에서 하차
>    * def step_2()
>        * robot이 앞으로 전진 가능하다면, 한 칸 전진
>        * 전진 조건 : 이동할 부분의 belt 내구도 != 0 and 해당 부분에 robot 부재
>        * 가장 먼저 belt에 올라간 robot부터 전진을 시작하므로 for문을 reverse로 순회
>        * step_1과 마찬가지로 robot이 끝 점에 도달하면 belt 하차. 동일 code지만 code자체 길이가 짧고, 사용 빈도가 낮아 따로 function화 하지는 않았음
>    * def step_3()
>        * belt의 시작점(idx = 0)에 robot을 올릴 수 있다면 robot 탑승
>        * 탑승 조건은 step_2의 전진 조건과 동일
>        * robot의 존재 여부 조건은 step_1에서 belt가 무조건 회전하므로 따로 체크할 필요성 없음
>    * main
>        * 종료 조건 (count_zero에서 check)에 부합하는 동안 step1~3반복
>        * belt가 총 몇 단계를 수행했는지 출력 후 종료
