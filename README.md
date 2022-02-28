# Algorithm_Study_2022

- 코딩테스트를 대비하기 위해 1주에 알고리즘 하나씩 타파하는 스터디입니다.
- 언어 : Python
- 참고 사이트 : [백준](https://www.acmicpc.net/) / [프로그래머스](https://programmers.co.kr/) / [Leetcode](https://leetcode.com/explore/) / [SW Expert Academy](https://swexpertacademy.com/)

## 스터디 방식

#### 1) 매 주 돌아가며 3문제 제출 및 발표를 한다.

- 문제는 순서인 사람이 해당 주 월요일 오전 8시 전까지 제출
  - 예시 : 다음주 그리디 담당인 A님은 다른분의 발표 이후 <br>
  - **`2/24 목요일`** ~ **`2/28일 월요일 오전 8시 전까지`** 문제 3개 먼저 제출. <br>
  - **`3/3 목요일`** 해당 주에 공부해온 알고리즘 md 파일 미리 업로드 및 모임시 발표

#### 2) 3문제는 난이도를 쉬움, 보통, 어려움 순으로 준비한다.

- **`쉬움`** : 백준 = 브론즈 ~ 실버 5 / 프로그래머스 = 레벨1
- **`보통`** : 백준 = 실버 4 ~ 실버 2 / 프로그래머스 = 레벨2
- **`어려움`** : 백준 = 실버 1 이상 / 프로그래머스 = 레벨3

#### 3) 발표는 마크다운 파일로 만들어 알고리즘 유형 폴더 안에 올린다.

- 아래의 **파일 및 폴더 구조** 내용 참고. 본인 폴더 아님

#### 4) 주 2회 모여서 코드리뷰와 알고리즘 설명을 한다.

- [1회차] 화요일 오후 9시전 (모임 X):

  - `쉬움`단계 1문제 풀어오고, 다른 사람 코드 리뷰 적기.
  - 궁금한 점, 개선점, 칭찬 등을 구체적으로 댓글로 남겨주세요 (말투는 서로 부드럽게 부탁드려요~)

- [2회차] 목요일 오후 9시 (모임 O) :

  - 모임 전까지 `보통`단계 1문제 풀어오고 다른 사람 코드 리뷰, 9시부터는 공부해온 알고리즘 발표 및 질문/답변 시간

- [3회차(유동)] 금요일 오후 9시 (모임 O) :
  - `어려움` 단계 문제를 시도해 본 사람들끼리 모여 코드리뷰. (못 풀었지만 시도한 코드를 올려도 괜찮습니다)

<br>

## 파일 및 폴더 구조

- 파일 이름 규칙 : 문제출처-문제번호-문제이름.py _(문제 번호 없으면 기재 X. 문제 이름 내에 공백이 있다면 \_ 로 구분)_
  - 예시 : `BOJ-1931-회의실_배정.py`
- 문제 풀이 코드가 있는 .py 파일은 **본인 폴더**에 넣기 (문제유형폴더 / 자기폴더 / 파이썬파일)
  - 예시 : 문제 푼 python 파일 -> `greedy` / `ohjiae` / `BOJ-1931-회의실_배정.py`
- 발표용 .md 파일은 **알고리즘 유형 폴더**에 넣기 (문제유형폴더 / 마크다운파일)
  - 예시 : 발표용 마크다운 파일 -> `greedy` / `Greedy-오지애.md`

<br>

## Commit Message Convention
- 예시 사진<br>

![commit-ex](https://user-images.githubusercontent.com/77822999/156032223-03b47b5f-2c09-41d0-95a9-6c4cb2037230.png)


#### 알고리즘 유형:[이슈번호] 작성자 - 문제이름

- 문제 커밋 예시 : `Greedy:[#23] ohjiae - 회의실 배정`
- 발표 커밋 예시 : `Greedy:[#23][#3][#4] ohjiae - 발표`
  <br>

## Pull Request Convention
- 예시 사진<br>



#### 알고리즘 유형:[이슈번호] 작성자 - (문제풀이/발표) 중 해당되는 것

- **문제 1개만** 풀었을 때 :
  - `Greedy:[#23] ohjiae - 문제풀이`
- **문제 다** 풀었을 때 :
  - `Greedy:[#23][#3][#4] ohjiae - 문제풀이`
- **발표와 문제풀이** 동시에 했을 때 :
  - `Greedy:[#4] ohjiae - 문제풀이,발표` (#4 이슈의 문제만 푼 경우임)
- **발표 파일만** 올릴 때 :
  - `Greedy:[#23][#3][#4] ohjiae - 발표` (모든문제 이슈번호 태그)
  <br>

## Issue Convention
- 예시 사진<br>

![issue-ex](https://user-images.githubusercontent.com/77822999/156030422-98f6aed0-28d9-4a7d-99f8-fc661ab66532.png)


#### [문제출처] 문제번호 - 문제이름 (발표자) _(문제 번호 없으면 기재 X)_

- 예시 : `[백준] 1931 - 회의실 배정 (오지애)`
- `[백준] 1003 - 피보나치 함수`
- `[프로그래머스] 체육복`


#### 태그 **3개** 달아주세요

- 태그는 대부분 생성되어 있으나, 없을 시 생성해서 추가해주세요 (영문 기본, 첫 글자 대문자)
  - 문제출처 : 백준 = `BOJ`, 프로그래머스 = `Programmers`, 릿코드 = `LeetCode`, 삼성 SWEA = `SWEA`
  - 알고리즘 유형 : `Greedy`, `DP`
  - 난이도 : `쉬움`, `보통`, `어려움`


## 참고

<details>
<summary>발표 순서 및 리뷰</summary>
<div markdown="1">
  
### 순서
  
|주차|이름(git_id)|발표일|
|---|------|--|
|1 주차|오레오라떼 (HaileyHyewonChung)|`3/3`|
|2 주차|도이(dyoon1635)|`3/10`|
|3 주차|제리 (yyj0128)|`3/17`|
|4 주차|머리 빗는 네오 (koodaeun)|`3/24`|
|5 주차|학부생 (kimdozzi)|`3/31`|
|6 주차|europani(europani)|`4/7`|
|7 주차|소담(soda)|`4/14`|
|8 주차|재재 (aegohc)|`4/21`|
|9 주차|튜브 (nayoung1124)|`4/28`|
|10 주차|프로도 (Choi-2022)|`5/5`|
|11 주차|무지(div-leejaemyeong)|`5/12`|

> 10 주차는 빨간날이니 추후에 고민해봅시다!

### 리뷰

> (예시) 2,3,4 를 리뷰해야 한다면?

> 2주차 담당자님(dyoon1635), 3주차 담당자님(제리), 4주차 담당자님(머리 빗는 네오) 의 코드를 리뷰하기!

| 이름    | 1.<br> 오레오(Hailey)   | 2.<br>doy (dyoon)        | 3.<br>제리(yyj01)          | 4.<br>네오 (kooda)          | 5.<br>학부생 (kimdo)   | 6.<br>euro (euro)           | 7.<br>소담 (soda)         | 8.<br>재재 (ohjiae)       | 9.<br>튜브 (nayoung)      | 10.<br>프로도 (Choi)    | 11.<br>무지 (div-lee)         |
| :----------: | :------------------: | :--------------------: | :-----------------------: | :--------------------: | :--------------------: | :--------------------: | :--------------------: | :--------------------: | :--------------------: | :------------------: | :-----------------------: |
| 1주차  | 도이<br>제리<br>네오 | 제리<br>네오<br>학부생 | 네오<br>학부생<br>유로 | 학부생<br>유로<br>소담 | 유로<br>소담<br>재재| 소담<br>재재<br>튜브| 재재<br>튜브<br>프로도 | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 |
| 2주차  | 제리<br>네오<br>학부생 | 네오<br>학부생<br>유로 | 학부생<br>유로<br>소담 | 유로<br>소담<br>재재 | 소담<br>재재<br>튜브 | 재재<br>튜브<br>프로도 | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 | 도이<br>제리<br>네오 |
| 3주차  | 네오<br>학부생<br>유로 | 학부생<br>유로<br>소담| 유로<br>소담<br>재재| 소담<br>재재<br>튜브 | 재재<br>튜브<br>프로도 | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 | 도이<br>제리<br>네오 | 제리<br>네오<br>학부생 |
| 4주차  | 학부생<br>유로<br>소담 | 유로<br>소담<br>재재 | 소담<br>재재<br>튜브 | 재재<br>튜브<br>프로도 | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 | 도이<br>제리<br>네오 | 제리<br>네오<br>학부생 | 네오<br>학부생<br>유로 |
| 5주차  | 유로<br>소담<br>재재 | 소담<br>재재<br>튜브 | 재재<br>튜브<br>프로도 | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 | 도이<br>제리<br>네오 | 제리<br>네오<br>학부생 | 네오<br>학부생<br>유로 | 학부생<br>유로<br>소담 |
| 6주차  | 소담<br>재재<br>튜브 | 재재<br>튜브<br>프로도 | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 | 도이<br>제리<br>네오 | 제리<br>네오<br>학부생 | 네오<br>학부생<br>유로 | 학부생<br>유로<br>소담 | 유로<br>소담<br>재재 |
| 7주차  | 재재<br>튜브<br>프로도 | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 | 도이<br>제리<br>네오 | 제리<br>네오<br>학부생 | 네오<br>학부생<br>유로 | 학부생<br>유로<br>소담 | 유로<br>소담<br>재재 | 소담<br>재재<br>튜브 |
| 8주차  | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 | 도이<br>제리<br>네오 | 제리<br>네오<br>학부생 | 네오<br>학부생<br>유로 | 학부생<br>유로<br>소담 | 유로<br>소담<br>재재 | 소담<br>재재<br>튜브 | 재재<br>튜브<br>프로도 |
| 9주차  | 프로도<br>무지<br>도이 | 무지<br>오레오<br>제리 | 오레오<br>도이<br>네오 | 도이<br>제리<br>학부생 | 제리<br>네오<br>유로 | 네오<br>학부생<br>소담 | 학부생<br>유로<br>재재 | 유로<br>소담<br>튜브 | 소담<br>재재<br>프로도 | 재재<br>튜브<br>무지 | 튜브<br>프로도<br>오레오 |
| 10주차 | 무지<br>도이<br>제리 | 오레오<br>제리<br>네오 | 도이<br>네오<br>학부생 | 제리<br>학부생<br>유로 | 네오<br>유로<br>소담 | 학부생<br>소담<br>재재 | 유로<br>재재<br>튜브 | 소담<br>튜브<br>프로도 | 재재<br>프로도<br>무지 | 튜브<br>무지<br>오레오 | 프로도<br>오레오<br>도이 |
| 11주차 | 도이<br>제리<br>네오 | 제리<br>네오<br>학부생 | 네오<br>학부생<br>유로 | 학부생<br>유로<br>소담 | 유로<br>소담<br>재재| 소담<br>재재<br>튜브| 재재<br>튜브<br>프로도 | 튜브<br>프로도<br>무지 | 프로도<br>무지<br>오레오 | 무지<br>오레오<br>도이 | 오레오<br>도이<br>제리 |

</div>
</details>
