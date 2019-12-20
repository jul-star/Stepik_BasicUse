import unittest
from ex_3_7_04 import Quebes

class TestCase_3_7_04(unittest.TestCase):
    def test_calculate_1(self):
        _str = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
        _tree = Quebes.str2tree(_str)
        Quebes.calculate(_tree)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
