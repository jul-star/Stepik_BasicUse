import unittest
from unittest.mock import patch
from ex_2_1_07 import Exceptions


class TestCase_2_1_07(unittest.TestCase):
    def test_ReadInput_1(self):
        _list = [4,
                 'ArithmeticError',
                 'ZeroDivisionError : ArithmeticError',
                 'OSError',
                 'FileNotFoundError : OSError']
        _Actual: list = []
        _Expected = [['ArithmeticError'],
                     ['ZeroDivisionError', ':', 'ArithmeticError'],
                     ['OSError'],
                     ['FileNotFoundError', ':', 'OSError']]
        with patch('builtins.input', side_effect=_list):
            _Actual = Exceptions.ReadInput()

        self.assertListEqual(_Actual, _Expected)

    def test_ReadInput_2(self):
        _list = [4,
                 'ArithmeticError',
                 'ZeroDivisionError : ArithmeticError',
                 'OSError',
                 'FileNotFoundError : OSError',
                 4,
                 'ZeroDivisionError',
                 'OSError',
                 'ArithmeticError',
                 'FileNotFoundError'
                 ]
        _Actual_1: list = []
        _Actual_2: list = []
        _Expected_1 = [['ArithmeticError'],
                       ['ZeroDivisionError', ':', 'ArithmeticError'],
                       ['OSError'],
                       ['FileNotFoundError', ':', 'OSError']]
        _Expected_2 = [['ZeroDivisionError'],
                       ['OSError'],
                       ['ArithmeticError'],
                       ['FileNotFoundError']]

        with patch('builtins.input', side_effect=_list):
            _Actual_1 = Exceptions.ReadInput()
            _Actual_2 = Exceptions.ReadInput()

        self.assertListEqual(_Actual_1, _Expected_1)
        self.assertListEqual(_Actual_2, _Expected_2)

    def test_getInheritance(self):
        _input = [['ArithmeticError'], ['ZeroDivisionError', ':', 'ArithmeticError']]
        _Expected = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError']}
        _Actual = Exceptions.getInheritance(_input)
        self.assertDictEqual(_Actual, _Expected)

    def test_getInheritance(self):
        _input = [['ArithmeticError'], ['ZeroDivisionError']]
        _Expected = ['ArithmeticError', 'ZeroDivisionError']
        _Actual = Exceptions.getCatches(_input)
        self.assertListEqual(_Actual, _Expected)

    def test_getCatches(self):
        _raw = [['ArithmeticError'], ['ZeroDivisionError']]
        _Expected = ['ArithmeticError', 'ZeroDivisionError']
        _Actual = Exceptions.getCatches(_raw)
        self.assertListEqual(_Actual, _Expected)

    def test_InConnection_1(self):
        _inheritance = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError']}
        # "next line only as info"
        _catches = ['ZeroDivisionError', 'ArithmeticError']
        _catch = 'ArithmeticError'
        _above = 'ZeroDivisionError'
        _Expected = False
        _Actual = Exceptions.InConnection(_catch, _above, _inheritance)
        self.assertEqual(_Actual, _Expected)

    def test_InConnection_2(self):
        _inheritance = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError']}
        # "next line only as info"
        _catches = ['ArithmeticError', 'ZeroDivisionError']
        _catch = 'ZeroDivisionError'
        _above = 'ArithmeticError'
        _Expected = True
        _Actual = Exceptions.InConnection(_catch, _above, _inheritance)
        self.assertEqual(_Actual, _Expected)

    def test_getExtra(self):
        _inh = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError']}
        _catches = ['ArithmeticError', 'ZeroDivisionError']
        _Expected = {'ArithmeticError': False, 'ZeroDivisionError': True}
        _Actual = Exceptions.getExtra(_inh, _catches)
        print("Actual: ", _Actual)
        self.assertDictEqual(_Actual, _Expected)

    def test_Find_1(self):
        _user_input = [4,
                       'ArithmeticError',
                       'ZeroDivisionError : ArithmeticError',
                       'OSError',
                       'FileNotFoundError : OSError',
                       4,
                       'ZeroDivisionError',
                       'OSError',
                       'ArithmeticError',
                       'FileNotFoundError']
        _Expected = ['FileNotFoundError']
        _extra = {}
        with patch('builtins.input', side_effect=_user_input):
            _extra = Exceptions.Find()
        _Actual = Exceptions.RefineExtra(_extra)
        self.assertListEqual(_Actual, _Expected)

    def test_Find_2(self):
        _user_input = [4,
                       'ArithmeticError',
                       'ZeroDivisionError : ArithmeticError',
                       'OSError',
                       'FileNotFoundError : OSError',
                       5,
                       'ZeroDivisionError',
                       'OSError',
                       'ArithmeticError',
                       'FileNotFoundError',
                       'FileNotFoundError']
        _Expected = ['FileNotFoundError']
        _extra = {}
        with patch('builtins.input', side_effect=_user_input):
            _extra = Exceptions.Find()
        _Actual = Exceptions.RefineExtra(_extra)
        self.assertListEqual(_Actual, _Expected)

    def test_Find_3(self):
        _user_input = [4,
                       'base',
                       'second : base',
                       'otherBase',
                       'first : otherBase',
                       4,
                       'base',
                       'otherbase',
                       'first',
                       'second']
        _Expected = ['first',
                     'second']
        _extra = {}
        with patch('builtins.input', side_effect=_user_input):
            _extra = Exceptions.Find()
        _Actual = Exceptions.RefineExtra(_extra)
        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
