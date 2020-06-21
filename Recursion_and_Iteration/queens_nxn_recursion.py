"""Placing N queens in a NxN chessboard in a way that all of them are safe"""


def place_n_queens(n, board):
    return n_queens(0, n, board)[1]


def n_queens(r, n, board):
    # base case, when queens have been placed in all rows
    if r == n:
        return True, board

    # else in the r-th row check for every box to find safe place
    for i in range(n):
        if is_safe(r, i, board):
            # if i-th column is safe to place queen, place the queen there
            # and check recursively for othre rows
            board[r][i] = 'q'
            okay, new_board = n_queens(r+1, n, board)

            if okay:
                return True, new_board
            board[r][i] = '-'
    return False, board


def is_safe(i, j, board):
    for c in range(len(board)):
        for r in range(len(board)):
            # check if i, j share row with any queen
            if board[c][r] == 'q' and i == c and j != r:
                return False
            # check if i, j share column with any queen
            elif board[c][r] == 'q' and j == r and i != c:
                return False
            # check if i, j share diagonal with any queen
            elif (i + j == c + r or i - j == c - r) and board[c][r] == 'q':
                return False
    return True


def main():
    n = 4
    board = [["-" for _ in range(n)] for _ in range(n)]
    q_board = place_n_queens(n, board)
    q_board = "\n".join(["".join(x) for x in q_board])
    print(q_board)


main()
