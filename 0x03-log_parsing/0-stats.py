#!/usr/bin/python3
"""Log parsing module
"""
import re
import sys


pattern = '^(\S+) - \[(\S+) (\S+)\] "GET \/projects\/260 HTTP\/1\.1" (\d+)\s(\d+)$'
def analyze(line: str = '', payload: dict = {}):
    """Analyze lines of input
    """
    if not line or type(line) is not str:
        return

    match = re.match(pattern, line)
    if not match:
        return
    payload['file_size'] += int(match.group(5))
    print(f"Line: {match.group(1)}\tFile size: {match.group(5)}") # test


if __name__ == '__main__':
    total_file_size = 0
    payload = {'file_size': 0}
    count = 0
    for line in sys.stdin:
        if line:
            analyze(line, payload)
        if count == 9:
            print("Total file size:", payload['file_size'])
            count = 0
        else:
            count += 1
