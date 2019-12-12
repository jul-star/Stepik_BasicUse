import unittest
from ex_3_3_12 import *


class TestCase_3_3_12(unittest.TestCase):
    def test_rpl2_1(self):
        _lines = [
            'There’ll be no more "Aaaaaaaaaaaaaaa"',
            'AaAaAaA AaAaAaA',
        ]
        _Actual = []
        _Expected = ['There’ll be no more "argh"',
                     'argh AaAaAaA',
                     ]
        for ln in _lines:
            _Actual.append(rpl2(ln))

        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
