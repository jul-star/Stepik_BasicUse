import unittest
from ex_1_6_07 import *

class TestCase_1_6_06(unittest.TestCase):
    def Check(self, Inheritance, Request, Expected):
        c = Connection()
        Actual = c.FindConnection(Inheritance, Request)
        self.assertEqual(len(Expected), len(Actual))
        for i in range(len(Expected)):
            self.assertEqual(Expected[i], Actual[i])

    def test_case_01(self):
        Inheritance = [['A', 'C', 'B'], ['B', 'D', 'E']]
        Request = ['E' 'A']
        Expected = [True]
        self.Check(Inheritance, Request, Expected)





