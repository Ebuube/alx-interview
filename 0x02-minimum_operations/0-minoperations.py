#!/usr/bin/python3
"""Minimum operations module"""
import math
import typing


def is_prime(n: int) -> bool:
    """
    Check if a positive integer is prime or not
    """
    if n < 2:
        return False

    for divisor in range(2, int(math.sqrt(n)) + 1):
        if n % divisor == 0:
            return False

    return True


def minOperations(n: int) -> int:
    """
    Find the minmum number of operations to be done
    """
    if type(n) is not int or n < 2:
        # Imposible to achieve or nothing required to do
        return 0

    if is_prime(n):
        return n

    min_operations: int = 0
    for min_factor in range(int(math.sqrt(n) + 1), 1, -1):
        # print(f"min_factor: {min_factor}")
        if n % min_factor == 0:
            min_operations = int(min_factor + (n / min_factor))
            break

    return min_operations
