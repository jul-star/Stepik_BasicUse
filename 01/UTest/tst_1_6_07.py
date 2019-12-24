import unittest
from ex_1_6_07 import *
from unittest.mock import patch


class TestCase_1_6_06(unittest.TestCase):
    def test_ReadInput_1(self):
        _list = [2, 'A : C B', 'B : D E']
        with patch('builtins.input', side_effect=_list):
            Actual = Connection.ReadInput()
            Expected = [['A', ':', 'C', 'B'], ['B', ':', 'D', 'E']]
            self.assertListEqual(Actual, Expected)

    def test_ReadInput_2(self):
        _list = [4, 'A', 'B : A', 'C : A', 'D : B C']
        with patch('builtins.input', side_effect=_list):
            Actual = Connection.ReadInput()
            Expected = [['A'], ['B', ':', 'A'], ['C', ':', 'A'], ['D', ':', 'B', 'C']]
            self.assertListEqual(Actual, Expected)

    def test_ReadInput_3(self):
        _list = [2, 'A C', 'B E']
        with patch('builtins.input', side_effect=_list):
            Actual = Connection.ReadInput()
            Expected = [['A', 'C'], ['B', 'E']]
            self.assertListEqual(Actual, Expected)

    def test_getInheritance_1(self):
        _raw = [['A', ':', 'C', 'B'], ['B', ':', 'D', 'E']]
        _Actual = Connection.getInheritance(_raw)
        _Expected = [['A', 'C', 'B'], ['B', 'D', 'E']]
        self.assertListEqual(_Actual, _Expected)

    def test_getInheritance_2(self):
        _raw = [['A'], ['B', ':', 'A'], ['C', ':', 'A'], ['D', ':', 'B', 'C']]
        _Actual = Connection.getInheritance(_raw)
        _Expected = [['A'], ['B', 'A'], ['C', 'A'], ['D', 'B', 'C']]
        self.assertListEqual(_Actual, _Expected)

    def test_BuildInheritance_1(self):
        _inh = [['A', 'C', 'B'], ['B', 'D', 'E']]
        _Actual = Connection.BuildInheritance(_inh)
        _Expected = {'A': ['C', 'B'], 'B': ['D', 'E']}
        self.assertDictEqual(_Actual, _Expected)

    def test_BuildInheritance_2(self):
        _inh = [['A'], ['B', 'A'], ['C', 'A'], ['D', 'B', 'C']]
        _Actual = Connection.BuildInheritance(_inh)
        _Expected = {'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
        self.assertDictEqual(_Actual, _Expected)

    def test_getRequest_1(self):
        _raw = [['E', 'A']]
        _Actual = Connection.getRequest(_raw)
        _Expected = [['E', 'A']]
        self.assertListEqual(_Actual, _Expected)

    def test_getRequest_2(self):
        _raw = [['E', 'A'], ['B', 'A'], ['C', 'A'], ['D', 'A']]
        _Actual = Connection.getRequest(_raw)
        _Expected = [['E', 'A'], ['B', 'A'], ['C', 'A'], ['D', 'A']]
        self.assertListEqual(_Actual, _Expected)

    def test_BuildRequest_1(self):
        _raw = [['E', 'A']]
        _Actual = Connection.BuildRequest(_raw)
        _Expected = [['E', 'A']]
        self.assertListEqual(_Actual, _Expected)

    def test_BuildRequest_2(self):
        _raw = [['E', 'A'], ['B', 'A'], ['C', 'A'], ['D', 'A']]
        _Actual = Connection.BuildRequest(_raw)
        _Expected = [['E', 'A'], ['B', 'A'], ['C', 'A'], ['D', 'A']]
        self.assertListEqual(_Actual, _Expected)

    def Check(self, inheritance: dict, requests: list, expected: list) -> None:
        """
        Helper Function
        :param inheritance:
        :param Inheritance: B is a child of A
        :param Request:  Is A parent of B?
        :param Expected: True/False
        :return: None
        """
        _Actual = Connection.FindInheritance(inheritance, requests)
        self.assertListEqual(_Actual, expected)

    def test_case_01(self):
        Inheritance = {'A': [], 'B': ['A']}
        Requests = [['A', 'B']]
        Expected = [True]
        self.Check(Inheritance, Requests, Expected)

    def test_case_02(self):
        Inheritance = {'A': [], 'B': ['A'], 'C': ['A'], 'D': ['B', 'C']}
        Requests = [['A', 'B'], ['B', 'D'], ['C', 'D'], ['D', 'A']]
        Expected = [True, True, True, False]
        self.Check(Inheritance, Requests, Expected)

    def test_case_03(self):
        Inheritance = {'A': ['C', 'B'], 'B': ['D', 'E']}
        Requests = [['E', 'A']]
        Expected = [True]
        self.Check(Inheritance, Requests, Expected)

    def test_case_04(self):
        Inheritance = {  # список введённых строк
            'G': ['F'],
            # сначала отнаследуем от F, потом его объявим, корректный алгоритм
            # все равно правильно обойдёт граф, независимо что было раньше:
            # наследование или объявление
            'A': [],
            'B': ['A'],
            'C': ['A'],
            'D': ['B', 'C'],
            'E': ['D'],
            'F': ['D'],
            # а теперь другая ветка наследования
            'X': [],
            'Y': ['X', 'A'],
            # свяжем две ветки наследования для проверки,
            # обошла ли рекурсия предков Z и предков Y в поисках A
            'Z': ['X'],
            'V': ['Z', 'Y'],
            'W': ['V']
        }

        Requests = [  # список введённых запросов
            ['A', 'G'],  # Yes   # A предок G через B/C, D, F
            ['A', 'Z'],  # No    # Y потомок A, но не Y
            ['A', 'W'],  # Yes   # A предок W через Y, V
            ['X', 'W'],  # Yes   # X предок W через Y, V
            ['X', 'QWE'],  # No    # нет такого класса QWE
            ['A', 'X'],  # No    # классы есть, но они нет родства :)
            ['X', 'X'],  # Yes   # родитель он же потомок
            ['1', '1'],  # No    # несуществующий класс
        ]

        Expected = [True, False, True, True, False, False, True, False]
        self.Check(Inheritance, Requests, Expected)

    def test_case_FindConnection_1(self):
        _user_input = [4, 'A', 'B : A', 'C : A', 'D : B C',
                       4, 'A B', 'B D', 'C D', 'D A']
        _Actual = []
        _Expected = [True, True, True, False]
        with patch('builtins.input', side_effect=_user_input):
            _Actual = Connection.FindConnection()
        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
