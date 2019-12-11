import sys
import re


def cat2(_line):
    pattern = r"(cat)"
    _mObj = re.findall(pattern, _line)
    if _mObj is not None and len(_mObj) > 1:
        return _line


for line in sys.stdin:
    line = line.rstrip()
    res = cat2(line)
    if res is not None:
        print(res)
