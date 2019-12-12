import unittest
from ex_3_3_08 import *


class MyTestCase(unittest.TestCase):
    def test_zz3_1(self):
        _lines = ['zabcz',
                  'zzz',
                  'zzxzz',
                  'zz',
                  'zxz',
                  'zzxzxxz', ]
        _Actual = []
        _Expected = ['zabcz',
                     'zzxzz', ]
        for ln in _lines:
            if zz3(ln):
                _Actual.append(ln)

        self.assertListEqual(_Actual, _Expected)

class MyTestCase(unittest.TestCase):
    def test_zz3_2(self):
        _lines = ['123zabcz456', ]
        _Actual = []
        _Expected = ['123zabcz456', ]
        for ln in _lines:
            if zz3(ln):
                _Actual.append(ln)

        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
