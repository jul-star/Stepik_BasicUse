import unittest
from ex_3_3_15 import *


class TestCase_3_3_15(unittest.TestCase):
    # def test_case_0(self):
    #     fnd15('10010')

    def test_rpl3_1(self):
        _lines = [
            '0',
            '10010',
            '00101',
            '01001',
            'Not a number',
            '1 1',
            '0 0',
        ]
        _Actual = []
        _Expected = [
            '0',
            '10010',
            '01001',
        ]
        for ln in _lines:
            if fnd15(ln):
                _Actual.append(ln)

        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
