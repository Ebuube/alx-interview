#!/usr/bin/env python3
"""Program to rotate an N x N 2D matrix 90 degrees clockwise
Solution:
    Firstly, transpose the matrix
    Secondly, Reverse each row of the matrix

This is a simple approach
Time complexity: O(n*n)
Space complexity: O(n*n)
"""
from typing import List


def transpose(matrix: List[List]) -> List[List]:
    """"
    1x1 eg. [[4]]
    2x2 eg. [[3, 4], [2, 1]]

    Condition:
        It must be a square matrix to work perfectly
    """
    length = len(matrix)
    trans = [[0 for col in range(length)] for row in range(length)]

    for row in range(length):
        for col in range(length):
            trans[col][row] = matrix[row][col]

    return trans


def rotate_matrix(matrix: List[List]) -> List[List]:
    """
    Condition:
        It must be a square matrix to work perfectly
    """
    rotated = transpose(matrix)
    for row in rotated:
        row = row.reverse()

    return rotated


# Test
matrix = [
        [0, 1, 2, 3],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]]
print("Initial matrix")
for row in matrix:
    print(row)
print

rotated = rotate_matrix(matrix)
print("Rotated matrix")
for row in rotated:
    print(row)
