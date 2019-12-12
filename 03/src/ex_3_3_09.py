import sys
import re


def backslash(_str):
    pattern = r"\\"
    return re.search(pattern, _str)


if __name__ == "__main__":
    for line in sys.stdin:
        if backslash(line):
            print(line, end='')
