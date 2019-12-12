import sys
import re


def rpl(_str):
    """
    В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
    :param _str:
    :return:
    """
    pattern = r"human"
    sub = r"computer"
    return re.sub(pattern, sub, _str)


if __name__ == "__main__":
    for line in sys.stdin:
        print(rpl(line), end='')
