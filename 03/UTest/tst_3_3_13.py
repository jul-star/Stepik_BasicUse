import unittest
from ex_3_3_13 import *


class TestCase_3_3_13(unittest.TestCase):
    def test_rpl3_1(self):
        _lines = [
            'this is a text',
            '"this\' !is. ?n1ce,',
        ]
        _Actual = []
        _Expected = [
            'htis si a etxt',
            '"htis\' !si. ?1nce,',
        ]
        for ln in _lines:
            _Actual.append(rpl3(ln))

        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
