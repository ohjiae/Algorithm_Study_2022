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