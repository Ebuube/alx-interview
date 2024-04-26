#!/usr/bin/python3
"""Program to rotate an N x N 2D matrix 90 degrees clockwise
Solution:
    Firstly, transpose the matrix
    Secondly, Reverse each row of the matrix
Time complexity: O(n*n)
Space complexity: O(n)
"""


def rotate_2d_matrix(matrix):
    """
    Condition:
        It must be a square matrix to work perfectly
    """
    length = len(matrix)

    for row in range(length):
        for col in range(row, length):
            (matrix[row][col], matrix[col][row]) = (matrix[col][row],
                                                    matrix[row][col])

    for row in range(length):
        matrix[row].reverse()
