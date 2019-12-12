import sys
import re


def tandemRepetitor(_str):
    """
    Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
    :param _str:
    :return: Boolean (find or not)
    """
    pattern = r"\b(\w+)\1\b"
    return re.search(pattern, _str) is not None


if __name__ == "__main__":
    for line in sys.stdin:
        if tandemRepetitor(line):
            print(line, end='')
