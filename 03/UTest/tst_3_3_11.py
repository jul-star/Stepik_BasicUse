import unittest
from ex_3_3_11 import *


class MyTestCase(unittest.TestCase):
    def test_rpl_1(self):
        _lines = [
            'I need to understand the human mind',
            'humanity',
        ]
        _Actual = []
        _Expected = ['I need to understand the computer mind',
                     'computerity',
                     ]
        for ln in _lines:
            _Actual.append(rpl(ln))

        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
