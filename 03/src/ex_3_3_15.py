import sys
import re


def fnd15(_str):
    """
    В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
    """
    pattern = r"([0,1])"
    fObj = re.findall(pattern, _str)
    if len(fObj) != len(_str):
        return False
    ln = len(_str)
    sum = 0
    for i in range(ln):
        if i % 2 == 0:
            sum += int(_str[i])
        else:
            sum -= int(_str[i])
    return sum%3 == 0


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        if fnd15(line):
            print(line)
