import unittest
from unittest.mock import patch
from ex_3_5_04 import Descendants


class TestCase_3_5_04(unittest.TestCase):
    def test_getInput_1(self):
        _user_input = [
            '[{"name": "A", "parents": []}, \
             {"name": "B", "parents": ["A", "C"]}, \
             {"name": "C", "parents": ["A"]}]']
        _Actual = []
        _Expected = [{'A': []},
                     {'B': ['A', 'C']},
                     {'C': ['A']}]
        with patch('builtins.input', side_effect=_user_input):
            _Actual = Descendants.getInput()
        self.assertEqual(_Expected, _Actual)

    def test_getInput_2(self):
        _user_input = [
            '[{"name": "B", "parents": ["A", "C"]}, \
            {"name": "C", "parents": ["A"]}, \
            {"name": "A", "parents": []}, \
            {"name": "D", "parents":["C", "F"]}, \
            {"name": "E", "parents":["D"]}, \
            {"name": "F", "parents":[]}]']
        _Actual = []
        _Expected = [{"B": ["A", "C"]},
                     {"C": ["A"]},
                     {"A": []},
                     {"D": ["C", "F"]},
                     {"E": ["D"]},
                     {"F": []}]
        with patch('builtins.input', side_effect=_user_input):
            _Actual = Descendants.getInput()
        self.assertEqual(_Expected, _Actual)

    def test_getClasses_1(self):
        _inh = [{'A': []},
                {'B': ['A', 'C']},
                {'C': ['A']}]
        _Expected = ['A', 'B', 'C']
        _Actual = Descendants.getClasses(_inh)
        self.assertListEqual(_Expected, _Actual)

    def test_getClasses_2(self):
        _inh = [{"B": ["A", "C"]},
                {"C": ["A"]},
                {"A": []},
                {"D": ["C", "F"]},
                {"E": ["D"]},
                {"F": []}]
        _Expected = ['A', 'B', 'C', 'D', 'E', 'F']
        _Actual = Descendants.getClasses(_inh)
        self.assertListEqual(_Expected, _Actual)

    def test_CalculateDescendats_1(self):
        _inh = [{'A': []}]
        _Expected = 1
        _Actual = Descendants.CalculateDescendats('A', _inh)
        self.assertEqual(_Expected, _Actual)

    def test_CalculateDescendats_2(self):
        _inh = [{'A': []},
                {'B': ['A', 'C']}]
        _Expected = 2
        _Actual = Descendants.CalculateDescendats('A', _inh)
        self.assertEqual(_Expected, _Actual)

    def test_CalculateDescendats_3(self):
        _inh = [{'A': []},
                {'B': ['A', 'C']},
                {'C': ['A']}]
        _Expected = 3
        _Actual = Descendants.CalculateDescendats('A', _inh)
        self.assertEqual(_Expected, _Actual)

    def test_CalculateDescendats_4(self):
        _inh = [{"B": ["A", "C"]},
                {"C": ["A"]},
                {"A": []},
                {"D": ["C", "F"]},
                {"E": ["D"]},
                {"F": []}]
        _Expected = 5
        _Actual = Descendants.CalculateDescendats('A', _inh)
        self.assertEqual(_Expected, _Actual)

    def test_Calculate_2(self):
        _inh = [{'A': []},
                {'B': ['A', 'C']},
                {'C': ['A']}]
        _desc = ['A', 'B', 'C']
        _Expected = {'A': 3, 'B': 1, 'C': 2}
        _Actual = Descendants.Calculate(_inh, _desc)
        self.assertDictEqual(_Expected, _Actual)

    def test_Calculate_1(self):
        _inh = [{"B": ["A", "C"]},
                {"C": ["A"]},
                {"A": []},
                {"D": ["C", "F"]},
                {"E": ["D"]},
                {"F": []}]
        _desc = ['A', 'B', 'C', 'D', 'E', 'F']
        _Expected = {'A': 5,
                     'B': 1,
                     'C': 4,
                     'D': 2,
                     'E': 1,
                     'F': 3}
        _Actual = Descendants.Calculate(_inh, _desc)
        self.assertDictEqual(_Expected, _Actual)


if __name__ == '__main__':
    unittest.main()
