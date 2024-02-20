#!/usr/bin/python3
"""
UTF-8 VALIDATION
"""

def char_bytes_len(one_byte):
    """
    Return the number of bytes this character codes for

    A continuation returns None
    """
    if one_byte >> 7 == 0b0:
        return 1    # A single-byte character

    bit_len = 5
    byte_count = 0b110

    while bit_len > 0:
        if one_byte >> bit_len == byte_count:
            return 8 - bit_len
        else:
            bit_len -= 1
            byte_count = (byte_count << 1) + 0b10

    print("Could not find len of expected characters")  # test
    return None


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    Return True if data is a valid UTF-8 encoding, else return False

    Each data set is a list of integers.
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer

    - CONCEPT -
    For a single-byte Character:
        * The byte starst with a `0`
        * It represents a single character in Unicode character set
    """
    if not isinstance(data, list):
        return False

    for num in data:
        if not isinstance(num, int):
            return False

        # Get only the least significant byte
        one_byte = num & 0xFF

        # Get the total number of bytes expected
        num_char = char_bytes_len(one_byte)
        print("Total char len: {}".format(num_char))    # test

    return True
