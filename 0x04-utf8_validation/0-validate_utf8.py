#!/usr/bin/python3
"""
UTF-8 VALIDATION
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Return True if data is a valid UTF-8 encoding, else return False

    Each data set is a list of integers.
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer
    """
    if not isinstance(data, list):
        return False

    for num in data:
        print("Testing: {}".format(num))    # test
        if not isinstance(num, int):
            return False

        one_byte = num & 0xFF

        if not ((one_byte >> 7) ^ 0b1):
            return False
    return True
