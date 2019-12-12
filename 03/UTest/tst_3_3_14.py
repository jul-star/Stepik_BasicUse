import unittest
from ex_3_3_14 import *


class TestCase_3_3_14(unittest.TestCase):
    def test_rpl4_1(self):
        _lines = [
            'attraction',
            'buzzzz',
        ]
        _Actual = []
        _Expected = [
            'atraction',
            'buz',
        ]
        for ln in _lines:
            _Actual.append(rpl4(ln))

        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
