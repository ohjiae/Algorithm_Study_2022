Simulation Algorithm
========================
# 1. Algorithm
> * 분류가 다소 애매
> * 보통은 제시된 기능 몇 가지를 구현
> * 문법 및 라이브러리에 익숙해지는데 가장 좋음
> * 메모리에 신경을 많이 써야 함

# 2. Problem & Code
 > ### -1. BOJ 1032 명령 프롬프트
> > (1) variable
> > > a) n : 파일 이름의 개수

> > > b) std : 기준 문자열

> > > c) chk : 각 문자열끼리 문자 하나하나가 같은지 check

> > (2) function
> > > a) def print_str(string, chk):
> > > > - 문자열 string과 boolean list chk를 parameter로 함
> > > > - string과 chk를 for문으로 검사하며 true면 문자출력, false면 ? 출력

> > > b) def chk_validation(std, chk, n):
> > > > - n개의 문자열을 입력으로 받으며,
> > > > - 기준 문자열 std와 각 문자를 비교하여 결과를 chk 리스트에 저장

> -2. BOJ 11866 요세푸스 문제 0

> > (1) variable

> > > a) n : 수열의 길이 

> > > b) k : Josephus step

> > > c) dq : 길이가 n이고 1부터 n까지의 정수를 담고 있음

> > (2) function

> > > a) def Josephus(dq, k):

> > > > - k step마다 dq의 원소를 하나씩 pop
> > > > - 원형수열을 가정하고 있으므로 rotate함수 사용

> -3. BOJ 2564 경비원

> > (1) variable 

> > > a) r, c : map의 가로 세로 size

> > > b) n : 상점의 개수

> > > c) shop : 각 상점의 위치를 저장. (Hash 함수를 통해 변형시킨 값을 넣음)

> > (2) function

> > > a) def Hash(x, y, r, c):

> > > > - r, c : map의 가로 세로 사이즈

> > > > - x, y : shop의 위치

> > > > - map을 일자형으로 보기위해 shop의 위치를 1차원으로 바꿔줌

> > > > - 북쪽 맨 왼쪽에서 시작. 시계 방향 회전

> > > b) def getDistance(my_pos, shop, r, c):

> > > > - r, c : map의 가로 세로 사이즈

> > > > - shop : 각 shop의 변환된 위치 정보에 대한 list

> > > > - my_pos : 현재 나의 위치

> > > > - 시계 방향으로 돌아가는 거리와 반시계 방향으로 돌아가는 거리 중 더 작은 값을 구함
