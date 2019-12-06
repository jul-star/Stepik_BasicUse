import unittest
from ex_2_1_09 import *

class MyTestCase(unittest.TestCase):
    def test_append01(self):
        lst = PositiveList()
        for i in range(100):
            try:
                lst.append(i+1)
            except Exception:
                self.assertEqual(True,False)

    def test_append_nonpositive(self):
        lst = PositiveList()
        for i in range(100):
            try:
                lst.append(-i)
            except Exception:
                self.assertEqual(True,True)



