Brute Force
===============
> * 모든 경우의 수를 전부 대입해보는 방식 (정확도 항상 보장)
> * 병렬 컴퓨팅이 가능한 경우 더 강력
> * DFS, BFS등의 탐색문제에서 전수 조사하는 경우가 많음
> * efficiency를 위해 중간중간 pruning을 하기도 함.


Problem 1 : BOJ_9663_ Nqueen

> * pruning이 중요한 문제
> * dfs로 brute force를 진행하며 불가능한 경우에는 더 이상 depth를 내려가지 않고 종료

```python
res = 0
N = int(input())
queens = [0] * N

def is_possible(x):
    for i in range(x):
        if (queens[i] == queens[x]) or \
            (abs(i - x) == abs(queens[i] - queens[x])):
            return False
    return True

def dfs(x):
    global res
    if x == N:
        res += 1
        return None

    for i in range(N):
        queens[x] = i
        if is_possible(x):
            dfs(x+1)

dfs(0)
print(res)
```


Problem 2:  BOJ_1759_ 암호 만들기
> * 반드시 모음1개, 자음2개 이상으로 구성된 암호 출력
> * 단순 brute force

```python
from itertools import combinations

l, c = map(int, input().split())
words = list(input().split())
res = set()

def check(pwd):
    vowel = ['a','e','i','o','u']
    wc1 = 0
    wc2 = 0
    for p in pwd:
        if p in vowel: wc1 += 1
        else: wc2 += 1
    if wc1 >= 1 and wc2 >= 2: return True
    return False


for pwd in combinations(words, l):
    if not check(pwd): continue

    pwd = sorted(pwd)
    tmp = ''
    for w in pwd: tmp += w
    res.add(tmp)
res = sorted(res)
for pwd in res: print(pwd)

```

Problem 3: 동전 뒤집기

> * bit masking문제
> * 각 bit로 뒤집을 row를 표시. bit를 1씩 올리며 iteration
> * row를 뒤집은 후엔, column은 T가 더 많은 경우에만 뒤집어줌

```python
import copy
from itertools import combinations

n = int(input())
res = n*n
board = []
for _ in range(n):
    tmp = input().split()
    row = []
    for t in tmp[0]:
        if t == 'H': row.append(1)
        else: row.append(-1)
    board.append(row)

def reverse(N):
    for i in range(len(N)):
        N[i] *= (-1)
    return N

def count(board):
    cnt = 0
    for each_row in board:
        for bit in each_row:
            if bit == -1: cnt += 1
    return cnt

def solve():
    global res
    for i in range(1, n+1):
        case = combinations(range(n), i)

        for each_case in case:
            tmp_board = copy.deepcopy(board)

            for each_row in each_case:
                tmp_board[each_row] = reverse(tmp_board[each_row])

            total = 0
            for col in range(n):
                cnt = 0
                for row in range(n):
                    if tmp_board[row][col] == -1: cnt += 1
                total = min(n - cnt, cnt)

            res = min(res, total)

if count(board) == 0:
    print(0)
    exit(0)
solve()
print(res)

```