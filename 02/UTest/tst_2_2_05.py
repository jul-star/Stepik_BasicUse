import unittest
from  ex_2_2_05 import *

class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual('2016 10 15', add('2016 10 05', 10))
        self.assertEqual('2016 10 15', add('2016 09 05', 40))
        self.assertEqual('2016 10 15', add('2015 10 15', 366))
        self.assertEqual('2016 10 15', add('2014 10 15', 366+365))

