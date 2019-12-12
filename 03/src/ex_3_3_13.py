import sys
import re

def rpl3(_str):
    """
    В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
    """
    pattern = r"\b(\w)(\w)"
    sub = r"\2\1"
    return re.sub(pattern, sub, _str)

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        print(rpl3(line))
