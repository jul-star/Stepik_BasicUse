import sys
import re


def rpl2(_str):
    """
    В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на слово "argh".
    :param _str:
    :return:
    """
    pattern = r"\b([a|A]+)\b"
    sub = r"argh"
    return re.sub(pattern, sub, _str, count=1)

if __name__ == "__main__":
    for line in sys.stdin:
        print(rpl2(line), end='')