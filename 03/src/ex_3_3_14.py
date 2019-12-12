import sys
import re


def rpl4(_str):
    """
    В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
    """
    pattern = r"(\w)\1{1,}"
    sub = r"\1"
    return re.sub(pattern, sub, _str)


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        print(rpl4(line))