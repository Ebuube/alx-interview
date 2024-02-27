#!/usr/bin/python3
"""N Queens"""
import sys
from pprint import pprint


def solveNQ(board, 0):
    """Solve the N Queen problem for a board starting from cell (0, 0)
    """
    pass


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

    pprint(get_board(arg))    # No need for pretty
    result = solveNQ(board)
    pprint(result)
