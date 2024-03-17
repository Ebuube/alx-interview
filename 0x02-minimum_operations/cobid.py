#!/usr/bin/python3
'''
contains the miniOperations methos
'''


def minOperations(n):
    '''
    calculates the minimum number of operations to get n number of Hs
    args:
        (n): an integer

    returns minumum number pf operations
    '''
    if n <= 1:
        return 0
    i = 2
    while i <= n:
        if n % i == 0:
            return minOperations(n // i) + i
        i += 1
    return n
