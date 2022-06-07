# Algorithm_Study_2022

- 코딩테스트를 대비하기 위해 함께 문제를 풀고 주 2회 코드리뷰를 하는 스터디입니다.
- 언어 : Python
- 참고 사이트 : [백준](https://www.acmicpc.net/) / [프로그래머스](https://programmers.co.kr/) / [Leetcode](https://leetcode.com/explore/) / [SW Expert Academy](https://swexpertacademy.com/)

<br>
<p>
</p>

## 스터디 방식

### 1. 매 주 아래 순서대로 5문제 제출 (금요일 오후 6시 전)
  
|순서|이름(git_id)|
|---|------|
|1|이재명(div-leejaemyeong)|
|2|소현(sohyeonnn)|
|3|김도윤(dyoon1635)|
|4|김은서(kimes9408)|
|5|김경민(jjongguet4u)|
|6|이호진(ili0820)|
|7|이은경(stat-eklee)|
|8|오지애(ohjiae)|

<br>
</br>  

### 2. 출제일별 난이도, 문제 수

> **화** : (필수) **`보통`** 1문제, **`어려움`** 1문제 / (선택) **`어려움`** 1문제<p>
  **목** : (필수) **`보통`** 1문제 / (선택) **`어려움`** 1문제

- 매 주 **해당일 오후 9시 전**까지 (필수) 문제 제출
- 깃허브로 Pull requests가 9시 전에 되어야 함
- 못 풀어도 시도한 코드라도 올려야 출석 인정

#### 난이도 기준
- **`보통`** : 백준 = 실버 1 ~ 골드 4
- **`어려움`** : 백준 = 골드 3 이상
- 프로그래머스는 재량껏 레벨2 이상 난이도 매겨주세요. 좋은 문제는 레벨 1도 가능

<br>
</br>  
  
### 3. 주 2회 **오후 9시** 코드 리뷰

- [1회차] 화요일 오후 9시:

  - `보통` 1문제, `어려움` 1문제 (+ 선택 1문제) 제출한 코드 리뷰

- [2회차] 목요일 오후 9시 :

  - `어려움` 1문제 (+ 선택 1문제) 제출한 코드 리뷰

- [3회차] 금요일 오후 6시 전까지 :

  - 해당주 출제자 : 이슈에 알고리즘 태그 입력
  - 다음주 출제자 : 5문제 제출 


<br>
</br>  

### 4. 보증금 제도
중간 이탈로 인해 스터디 분위기가 망가지는 것을 방지하기 위해, 보증금제를 진행합니다.

> 보증금 : 총 2만원 ('참여 보증금' 1만원, '벌금 차감용' 1만원)

- `참여 보증금` : 한 달동안 참여 조건의 보증금. 중간 이탈시 돌려주지 않음
- `벌금 차감용` : 
  - 1회차 불참 = **1000원** 차감
  - 2회차 불참 = **1500원** 차감 (가중치 부여)
  - (주 2회 연속 불참시 **총 2500원** 차감)

<br>

**매 달 말일, 다음달 참여 여부를 여쭤봅니다.**
이 때 스터디 탈퇴시에는 '참여 보증금'을 돌려드립니다. 중간 이탈시에만 돌려드리지 않아요.
탈퇴하는 인원이 있을 경우,탈퇴할 분에게는 `보증금 2만원 - 벌금` 으로 돌려드리고 (중간이탈자는 벌금뺀 나머지 금액만 돌려줌), 
돌려드리고 남은 금액 > 0 이면, N분의 1로 나누어 가집니다 (벌금자 제외 나머지 인원 = N)

<br>
<p>
</p>



## 파일 및 폴더 구조

- 파일 이름 규칙 : 문제출처-문제번호-문제이름.py _(문제 번호 없으면 기재 X. 문제 이름 내에 공백이 있다면 \_ 로 구분)_
  - 예시 : `BOJ-1931-회의실_배정.py`

- .py 파일은 **본인 폴더**에 넣기 (all_users / 자기폴더 / 파이썬 파일)
  - 예시 : 문제 푼 python 파일 -> `all_users` / `ohjiae` / `BOJ-1931-회의실_배정.py`

<br>
<p>
</p>

## Commit Message Convention
### 난이도: [이슈번호] 문제이름, [이슈번호] 문제이름 - 본인 이름

- 커밋 예시 : `보통: [#23] 피보나치 함수, [#24] 회의실 배정 - 오지애`
- 커밋 예시 : `어려움: [#25] 달팽이 - 오지애`
- **보통과 어려움 난이도 따로 커밋해주세요**

<br>
<p>
</p>

## Pull Request Convention
- 예시 사진<br>

<br>
<p>
</p>

## Issue Convention
#### [문제출처] 문제번호 - 문제이름

- 예시 : `[백준] 1931 - 회의실 배정`
- `[백준] 1003 - 피보나치 함수`
- `[프로그래머스] 42682 - 체육복`
  - 프로그래머스는 보통 url에 문제번호 있음

<p>
</p>

#### 태그 **3개** 달아주세요

- 태그는 대부분 생성되어 있으나, 없을 시 생성해서 추가해주세요 (영문 기본, 첫 글자 대문자)
  - 문제출처 : 백준 = `BOJ`, 프로그래머스 = `Programmers`, 릿코드 = `LeetCode`, 삼성 SWEA = `SWEA`
  - 난이도 : `보통`, `어려움`
- 문제 다 푼 후 **금요일 오후 6시 이후** 알고리즘 유형 공개 => 태그 입력.
  - 알고리즘 유형 : `Greedy`, `DP`
  
- 예시 사진<br>

![issue-ex](https://user-images.githubusercontent.com/77822999/156030422-98f6aed0-28d9-4a7d-99f8-fc661ab66532.png)
