import unittest
import inspect
from my_func import *

class TestCaseMyFunc(unittest.TestCase):
    def test_my_func001(self):
        self.assertEqual(div(3,2), 1.5)
        print(self.__class__.__name__ + ": " + inspect.stack()[0][3])


