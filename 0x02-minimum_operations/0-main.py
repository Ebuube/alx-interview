#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

for n in range(0, 30):
    print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))
