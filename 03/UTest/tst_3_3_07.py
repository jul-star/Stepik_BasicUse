import unittest
from ex_3_3_07 import *


class TestCase_3_3_07(unittest.TestCase):
    def test_cat3_1(self):
        _lines = ['cat',
                  'catapult and cat',
                  'catcat',
                  'concat',
                  'Cat',
                  '"cat"',
                  '!cat?', ]
        _Actual = []
        _Expected = ['cat',
                     'catapult and cat',
                     '"cat"',
                     '!cat?', ]
        for ln in _lines:
            if cat3(ln):
                _Actual.append(ln)

        self.assertListEqual(_Actual, _Expected)

    def test_cat3_1(self):
        _lines = ['cat',
                  'catapult and cat',
                  'catcat',
                  'concat',
                  'Cat',
                  '"cat"',
                  '!cat?', ]
        _Actual = []
        _Expected = ['cat',
                     'catapult and cat',
                     '"cat"',
                     '!cat?', ]
        for ln in _lines:
            if cat3(ln):
                _Actual.append(ln)

        self.assertListEqual(_Actual, _Expected)

if __name__ == '__main__':
    unittest.main()
