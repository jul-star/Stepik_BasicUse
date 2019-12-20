import unittest
from ex_3_7_04 import Quebes


class TestCase_3_7_04(unittest.TestCase):
    def test_calculate_1(self):
        _str = '<cube color="blue"><cube color="red" id="100"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
        _root = Quebes.str2tree(_str)
        _dict = {'red': 0,
                 'green': 0,
                 'blue': 0}
        worth: int = 1
        Quebes.addWorth(_dict, _root.attrib, worth)
        Quebes.calculate(_root, worth, _dict)
        print("Output: ", _dict)
        Expected = {'red': 4,
                    'green': 3,
                    'blue': 1}
        self.assertDictEqual(_dict, Expected)

    def test_calculate_2(self):
        _str = '<cube color="blue"><cube color="red"><cube color="green"><cube color="green"><cube color="green"><cube color="blue"></cube><cube color="green"></cube><cube color="red"></cube></cube></cube></cube></cube><cube color="red"><cube color="blue"></cube></cube></cube>'

        _root = Quebes.str2tree(_str)
        _dict = {'red': 0,
                 'green': 0,
                 'blue': 0}
        worth: int = 1
        Quebes.addWorth(_dict, _root.attrib, worth)
        Quebes.calculate(_root, worth, _dict)
        print("Output: ", _dict)
        Expected = {'red': 10,
                    'green': 18,
                    'blue': 10}
        self.assertDictEqual(_dict, Expected)

    def test_calculate_3(self):
        _str = '<cube color="blue"><cube color="red"><cube color="green"><cube color="blue"><cube color="red"><cube color="red"></cube></cube></cube></cube></cube><cube color="blue"><cube color="green"></cube></cube><cube color="blue"></cube></cube>'
        _root = Quebes.str2tree(_str)
        _dict = {'red': 0,
                 'green': 0,
                 'blue': 0}
        worth: int = 1
        Quebes.addWorth(_dict, _root.attrib, worth)
        Quebes.calculate(_root, worth, _dict)
        print("Output: ", _dict)
        Expected = {'red': 13,
                    'green': 6,
                    'blue': 9}
        self.assertDictEqual(_dict, Expected)


if __name__ == '__main__':
    unittest.main()
