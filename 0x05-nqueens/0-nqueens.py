#!/usr/bin/python3
"""N Queens"""
import sys
from pprint import pprint


def conv_to_perm(board):
    """Print one of the permutations of the result
    """
    if not board or len(board) == 0:
        print([])
        return

    result = []
    for row in range(len(board)):
        col = board[row].index(1)
        result.append(col)

    return result


def conv_to_soln(board):
    """Print ALX acceptable solution of the result
    """
    if not board or len(board) == 0:
        print([])
        return

    result = []
    for row in range(len(board)):
        col = board[row].index(1)
        result.append([row, col])

    return result


def is_safe(board, row, col):
    """Check if the current board setting is safe for all queens
    """
    # Check horizontally across and leftwards
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check diagonally left and upwards
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    # Check diagonally left and downwards
    for r, c in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    return True


def solveNQ(board, col):
    """Solve the N Queen problem for a board starting from cell (0, 0)
    """
    if col >= len(board):
        return True

    for row in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen in this position
            board[row][col] = 1

            # Recursively attempt to place the rest of the queens
            if solveNQ(board, col + 1) is True:
                return True

            # If that didn't, nullify the current Queen's position
            board[row][col] = 0

    return False


def get_board(size):
    """Create and return the Chess board to solve
    """
    board = []
    for i in range(size):
        row = []
        for x in range(size):
            row.append(0)
        board.append(row)

    return board


if __name__ == '__main__':
    MIN_QUEENS = 4

    arg_len = len(sys.argv) - 1
    if arg_len != 1:
        print("Usage: nqueens N")
        exit(1)

    arg = sys.argv[1]
    if not arg.isdecimal():
        print("N must be a number")
        exit(1)

    arg = int(arg)
    if arg < MIN_QUEENS:
        print("N must be at least 4")
        exit(1)

    board = get_board(arg)
    print("Board:")
    pprint(board)    # No need for pretty

    result = solveNQ(board, 0)
    print("Is there a solution: {}".format(result))

    print("Board:")
    pprint(board)

    print("\nSolution: -> ")
    pprint(conv_to_soln(board))

    print("\nOne permutaion: -> ")
    pprint(conv_to_perm(board))
