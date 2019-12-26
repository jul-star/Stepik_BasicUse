import unittest
from unittest.mock import patch
from io import StringIO
from ex_3_5_04 import Descendants


class TestCase_3_5_04(unittest.TestCase):
    def test_getInput_1(self):
        _user_input = [
            '[{"name": "A", "parents": []}, \
            {"name": "B", "parents": ["A", "C"]}, \
            {"name": "C", "parents": ["A"]}]']
        _Actual = []
        _Expected = {'A': [],
                     'B': ['A', 'C'],
                     'C': ['A']}
        with patch('builtins.input', side_effect=_user_input):
            _Actual = Descendants.getInput()
        self.assertEqual(_Expected, _Actual)

    def test_getInput_3(self):
        _user_input = [
            '[{"name": "G", "parents": ["F"]}, \
            {"name": "A", "parents": []}, \
            {"name": "B", "parents": ["A"]}, \
            {"name": "C", "parents": ["A"]}, \
            {"name": "D", "parents": ["B", "C"]}, \
            {"name": "E", "parents": ["D"]}, \
            {"name": "F", "parents": ["D"]}, \
            {"name": "X", "parents": []}, \
            {"name": "Y", "parents": ["X", "A"]}, \
            {"name": "Z", "parents": ["X"]}, \
            {"name": "V", "parents": ["Z", "Y"]}, \
            {"name": "W", "parents": ["V"]}]']
        _Actual = []
        _Expected = {'G': ['F'], 'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C'], 'E': ['D'], 'F': ['D'], 'X': [],
                     'Y': ['X', 'A'], 'Z': ['X'], 'V': ['Z', 'Y'], 'W': ['V']}
        with patch('builtins.input', side_effect=_user_input):
            _Actual = Descendants.getInput()
        self.assertEqual(_Expected, _Actual)

    def test_getClasses_1(self):
        _inh = {'A': [],
                'B': ['A', 'C'],
                'C': ['A']}
        _Expected = ['A', 'B', 'C']
        _Actual = Descendants.getClasses(_inh)
        self.assertListEqual(_Expected, _Actual)

    def test_getClasses_2(self):
        _inh = {"B": ["A", "C"],
                "C": ["A"],
                "A": [],
                "D": ["C", "F"],
                "E": ["D"],
                "F": []}
        _Expected = ['A', 'B', 'C', 'D', 'E', 'F']
        _Actual = Descendants.getClasses(_inh)
        self.assertListEqual(_Expected, _Actual)

    def test_inh2graph_1(self):
        _inh = {'A': [],
                'B': ['A', 'C'],
                'C': ['A']}
        _Expected = {'A': ['A', 'B', 'C'], 'B': ['B'], 'C': ['B', 'C']}
        _Actual = Descendants.inh2graph(_inh)
        self.assertDictEqual(_Expected, _Actual)

    def test_inh2graph_2(self):
        _inh = {"B": ["A", "C"],
                "C": ["A"],
                "A": [],
                "D": ["C", "F"],
                "E": ["D"],
                "F": []}
        _Expected = {'A': ['A', 'B', 'C'], 'B': ['B'], 'C': ['B', 'C', 'D'], \
                     'D': ['D', 'E'], 'E': ['E'], 'F': ['D', 'F']}
        _Actual = Descendants.inh2graph(_inh)
        self.assertDictEqual(_Expected, _Actual)

    def test_CountDescendats_1(self):
        _graph = {'A': ['A']}
        _Expected = 1
        _parent = 'A'
        _Actual = Descendants.CountDescendats(_parent, _graph)
        self.assertEqual(_Expected, _Actual)

    def test_CountDescendats_2(self):
        _graph = {'A': ['A', 'B'],
                  'B': []}
        _Expected = 2
        _parent = 'A'
        _Actual = Descendants.CountDescendats(_parent, _graph)
        self.assertEqual(_Expected, _Actual)

    def test_CountDescendats_3(self):
        _graph = {'A': ['A', 'B', 'C'], 'B': ['B'], 'C': ['B', 'C']}
        _Expected = 3
        _parent = 'A'
        _Actual = Descendants.CountDescendats(_parent, _graph)
        self.assertEqual(_Expected, _Actual)

    def test_CountDescendats_4(self):
        _graph = {'A': ['A', 'B', 'C'], 'B': ['B'], 'C': ['B', 'C', 'D'], \
                  'D': ['D', 'E'], 'E': ['E'], 'F': ['D', 'F']}
        _Expected = 5
        _parent = 'A'
        _Actual = Descendants.CountDescendats(_parent, _graph)
        self.assertEqual(_Expected, _Actual)

    def test_Count_2(self):
        _graph = {'A': ['A', 'B', 'C'], 'B': ['B'], 'C': ['B', 'C']}
        _desc = ['A', 'B', 'C']
        _Expected = {'A': 3, 'B': 1, 'C': 2}
        _Actual = Descendants.Count(_graph, _desc)
        self.assertDictEqual(_Expected, _Actual)

    def test_Count_1(self):
        _graph = {'A': ['A', 'B', 'C'], 'B': ['B'], 'C': ['B', 'C', 'D'], \
                  'D': ['D', 'E'], 'E': ['E'], 'F': ['D', 'F']}
        _desc = ['A', 'B', 'C', 'D', 'E', 'F']
        _Expected = {'A': 5,
                     'B': 1,
                     'C': 4,
                     'D': 2,
                     'E': 1,
                     'F': 3}
        _Actual = Descendants.Count(_graph, _desc)
        self.assertDictEqual(_Expected, _Actual)

    def test_run_1(self):
        _user_input = ['[{"name": "B", "parents": ["A", "C"]}, \
        {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, \
         {"name": "D", "parents":["C", "F"]}, \
          {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]']
        _Expected = 'A : 5\n' \
                    'B : 1\n' \
                    'C : 4\n' \
                    'D : 2\n' \
                    'E : 1\n' \
                    'F : 3\n'
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                Descendants.run()
                _Actual = fake_out.getvalue()

        self.assertEqual(_Expected, _Actual)

    def test_run_2(self):
        _user_input = [
            '[{"name": "G", "parents": ["F"]}, \
            {"name": "A", "parents": []}, \
            {"name": "B", "parents": ["A"]}, \
            {"name": "C", "parents": ["A"]}, \
            {"name": "D", "parents": ["B", "C"]}, \
            {"name": "E", "parents": ["D"]}, \
            {"name": "F", "parents": ["D"]}, \
            {"name": "X", "parents": []}, \
            {"name": "Y", "parents": ["X", "A"]}, \
            {"name": "Z", "parents": ["X"]}, \
            {"name": "V", "parents": ["Z", "Y"]}, \
            {"name": "W", "parents": ["V"]}]']
        _Expected = 'A : 10\n' \
                    'B : 5\n' \
                    'C : 5\n' \
                    'D : 4\n' \
                    'E : 1\n' \
                    'F : 2\n' \
                    'G : 1\n' \
                    'V : 2\n' \
                    'W : 1\n' \
                    'X : 5\n' \
                    'Y : 3\n' \
                    'Z : 3\n'
        _Actual = None
        with patch('builtins.input', side_effect=_user_input):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                Descendants.run()
                _Actual = fake_out.getvalue()

        self.assertEqual(_Expected, _Actual)


if __name__ == '__main__':
    unittest.main()
