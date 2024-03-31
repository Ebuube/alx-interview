#!/usr/bin/python3
"""Log parsing module
"""
import re
import sys

old_pattern = r'\A(\d+\.\d+\.\d+\.\d+) - \[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)\Z'

new_pattern = r'(\w+) (\w+) "GET /projects/260 HTTP/1\.1 (\d+) (\d+)'

prev_pattern = r'^<(\d+\.\d+\.\d+\.\d+)> - \[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$'

next_pattern = r'(\S+)\s+-\s+\[(\d+\-\d+\-\d+\s*\d+:\d+:\d+\.\d+)\] [^"]*" (\d{3}) (\d+)'

pattern = '^(\S+) - \[(\S+) (\S+)\] "GET \/projects\/260 HTTP\/1\.1" (\d+)\s(\d+)$'
for line in sys.stdin:
    if line:
        print("Line:", line)    # test
        match = re.match(pattern, line)
        print("Match:", match)  # test
        if not match:
            continue
        for i in range(1, 6):
            print(match.group(i), end='')
        print()
