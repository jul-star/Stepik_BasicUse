import re
import sys


def cat3(_str):
    pattern = r"\b(cat)\b";
    if len(re.findall(pattern, _str)) > 0:
        return True
    return False


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        if cat3(line):
            print(line)
