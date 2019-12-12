import unittest
from ex_3_3_09 import *


class TestCaseBSlash(unittest.TestCase):
    def test_backslash_1(self):
        _lines = ['\w denotes word character',
                  'No slashes here', ]
        _Actual = []
        _Expected = ['\w denotes word character', ]
        for ln in _lines:
            if backslash(ln):
                _Actual.append(ln)

        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
