#!/usr/bin/python3
"""
An implementation of Pascal Triangle generator
"""


def pascal_triangle(n):
    """
    Generate a Pascal trinagle of n
    # Assumption: n is always an integer
    """
    if type(n) is not int or n <= 0:
        return []

    triangle = [[1]]

    for i in range(n - 1):
        newRow = [1]    # Starts with 1
        for x in range(len(triangle[i]) - 1):
            cur = triangle[i][x]
            next = triangle[i][x + 1]
            newRow.append(cur + next)
        # Append new Row
        newRow.append(1)    # Ends with 1
        triangle.append(newRow)

    return triangle
