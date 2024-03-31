#!/usr/bin/python3
"""Test pattern matching
"""
import re

pattern = r"\A(\w+)\s+(\d+)\s+(\w+)\Z"
sample_string = "Ebube 14 Gideon Hello 14 World"

match = re.match(pattern, sample_string)

if match:
    name1 = match.group(1)
    number = match.group(2)
    name2 = match.group(3)

    # Print the extracted information
    print("Name 1:", name1)
    print("Name 2:", name2)
    print("Number:", number)
else:
    print("Sample string does not conform to the pattern")
