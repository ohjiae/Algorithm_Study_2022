import math
def dp(board):
    n, m = len(board), len(board[0])
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] > 0:
                tmp = min(board[i-1][j], board[i][j-1], board[i-1][j-1])
                tmp = int(math.sqrt(tmp))

                board[i][j] = int(math.pow(tmp+1, 2))

    #for i in range(n):
    #    print(board[i])

    print(max(list(map(max, board))))

if __name__ == "__main__":
    n, m = map(int, input().split())
    board = []
    board.append(list('0' * (m+1)))
    for _ in range(n):
        board.append(list('0'+input()))

    for i in range(len(board)):
        board[i] = list(map(int, board[i]))
    dp(board)