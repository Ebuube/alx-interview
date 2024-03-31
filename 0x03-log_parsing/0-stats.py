#!/usr/bin/python3
"""Log parsing module
"""
import re
import signal
import sys


line_counter = 0
payload = {
        'file_size': 0,
        'status_codes': {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                         '404': 0, '405': 0, '500': 0}}


def sigint_handler(signal, frame):
    """Handle SIGINT
    Also known as Keyboard Interrupt
        - Print metrics on event
    """
    print_metrics(payload)
    line_counter = 0


def analyze(line: str = '', payload: dict = {}):
    """Analyze lines of input
    """
    if not line or type(line) is not str:
        return

    pattern = '^(\S+) - \[(\S+) (\S+)\] "GET \/projects\/260 HTTP\/1\.1" (\d+)\s(\d+)$'     # noqa: W605, E501
    match = re.match(pattern, line)
    if not match:
        return
    file_size = int(match.group(5))
    status_code = match.group(4)

    # Updating metrics
    payload['file_size'] += file_size
    if status_code in payload['status_codes']:
        payload['status_codes'][status_code] += 1


def print_metrics(payload: dict = {}):
    """Display the metrics in Payload
    """
    if not payload:
        return
    try:
        print("File size:", payload['file_size'])
    except KeyError:
        pass

    try:
        for status_code, amount in payload['status_codes'].items():
            if amount > 0:
                print(f"{status_code}: {amount}")
    except KeyError:
        pass


if __name__ == '__main__':
    """
    Analyze a stream of inputs

    After every 10 lines/keyboard interrupt print metrics
    """
    for line in sys.stdin:
        if not line or len(line) == 0:
            continue
        analyze(line, payload)
        if line_counter == 9:
            print_metrics(payload)
            line_counter = 0
        else:
            line_counter += 1
