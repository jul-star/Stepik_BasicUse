import unittest
from ex_2_3_04 import *

def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0

a = [i for i in range(31)] # [0, 1, 2, ... , 30]

class MyTestCase(unittest.TestCase):

    def CheckActualVsExpected(self, Actual, Expected):
        self.assertEqual(len(Actual), len(Expected))
        self.assertListEqual(Actual, Expected)

    def test_any(self):
        Actual = list(multifilter(a, mul2, mul3, mul5))
        Expected = [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]
        self.CheckActualVsExpected(Actual, Expected)

    def test_half(self):
        Actual = list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))
        Expected = [0, 6, 10, 12, 15, 18, 20, 24, 30]
        self.CheckActualVsExpected(Actual, Expected)

    def test_all(self):
        Actual = list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))
        Expected = [0, 30]
        self.CheckActualVsExpected(Actual, Expected)

if __name__ == '__main__':
    unittest.main()
