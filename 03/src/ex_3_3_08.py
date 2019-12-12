import sys
import re


def zz3(_str):
    """
    Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
    :param _str:
    :return: True/False
    """
    # pattern = r"(z.{3}z)"
    # return len(re.findall(pattern, _str)) > 0
    pattern = r"z.{3}z"
    return re.search(pattern, _str) is not None


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        if zz3(line):
            print(line)
