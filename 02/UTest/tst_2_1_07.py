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

    def test_ReadInput_2(self):
        _list = [4,
                 'base',
                 'second : base',
                 'otherbase',
                 'first : otherbase',
                 4,
                 'base',
                 'otherbase',
                 'first',
                 'second']
        _Actual_1: list = []
        _Actual_2: list = []
        _Expected_1 = [['base'],
                       ['second', ':', 'base'],
                       ['otherbase'],
                       ['first', ':', 'otherbase']]
        _Expected_2 = [['base'],
                       ['otherbase'],
                       ['first'],
                       ['second']]

        with patch('builtins.input', side_effect=_list):
            _Actual_1 = Exceptions.ReadInput()
            _Actual_2 = Exceptions.ReadInput()

            _user_input = []

    def test_ReadInput_3(self):
        _list = [4,
                 "BaseException",
                 "Exception : BaseException",
                 "LookupError : Exception",
                 "KeyError : LookupError",
                 2,
                 "BaseException",
                 "KeyError"]
        _Actual_1: list = []
        _Actual_2: list = []
        _Expected_1 = [['BaseException'],
                       ['Exception', ':', 'BaseException'],
                       ['LookupError', ':', 'Exception'],
                       ['KeyError', ':', 'LookupError']]
        _Expected_2 = [['BaseException'],
                       ['KeyError']]

        with patch('builtins.input', side_effect=_list):
            _Actual_1 = Exceptions.ReadInput()
            _Actual_2 = Exceptions.ReadInput()

    def test_getInheritance_2(self):
        _input = [['base'],
                  ['second', ':', 'base'],
                  ['otherbase'],
                  ['first', ':', 'otherbase']]
        _Expected = {'base': [], 'second': ['base'],
                     'otherbase': [], 'first': ['otherbase']}
        _Actual = Exceptions.getInheritance(_input)
        self.assertDictEqual(_Actual, _Expected)

    def test_getInheritance_1(self):
        _input = [['BaseException'],
                  ['Exception', ':', 'BaseException'],
                  ['LookupError', ':', 'Exception'],
                  ['KeyError', ':', 'LookupError']]
        _Expected = {'BaseException': [],
                     'Exception': ['BaseException'],
                     'LookupError': ['Exception'],
                     'KeyError': ['LookupError'],
                     }
        _Actual = Exceptions.getInheritance(_input)
        self.assertDictEqual(_Actual, _Expected)

    def test_getInheritance_3(self):
        _input = [['ArithmeticError'], ['ZeroDivisionError', ':', 'ArithmeticError']]
        _Expected = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError']}
        _Actual = Exceptions.getInheritance(_input)
        self.assertDictEqual(_Actual, _Expected)

    def test_getCatches_1(self):
        _input = [['ArithmeticError'], ['ZeroDivisionError']]
        _Expected = ['ArithmeticError', 'ZeroDivisionError']
        _Actual = Exceptions.getCatches(_input)
        self.assertListEqual(_Actual, _Expected)

    def test_getCatches_2(self):
        _raw = [['ArithmeticError'], ['ZeroDivisionError']]
        _Expected = ['ArithmeticError', 'ZeroDivisionError']
        _Actual = Exceptions.getCatches(_raw)
        self.assertListEqual(_Actual, _Expected)

    def test_getCatches_3(self):
        _raw = [['base'],
                ['otherbase'],
                ['first'],
                ['second']]
        _Expected = ['base', 'otherbase', 'first', 'second']
        _Actual = Exceptions.getCatches(_raw)
        self.assertListEqual(_Actual, _Expected)

    def test_getCatches_4(self):
        _raw = [['BaseException'],
                ['KeyError']]
        _Expected = ['BaseException', 'KeyError']
        _Actual = Exceptions.getCatches(_raw)
        self.assertListEqual(_Actual, _Expected)

    def test_InConnection_1(self):
        _inheritance = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError']}
        # "next line only as info'
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

    def test_InConnection_3(self):
        _inheritance = {'base': [], 'second': ['base'],
                        'otherbase': [], 'first': ['otherbase']}
        _catch = 'second'
        _above = 'base'
        _Expected = True
        _Actual = Exceptions.InConnection(_catch, _above, _inheritance)
        self.assertEqual(_Actual, _Expected)

    def test_InConnection_4(self):
        _inheritance = {'base': [], 'second': ['base'],
                        'otherbase': [], 'first': ['otherbase']}
        _catch = 'first'
        _above = 'otherbase'
        _Expected = True
        _Actual = Exceptions.InConnection(_catch, _above, _inheritance)
        self.assertEqual(_Actual, _Expected)

    def test_InConnection_5(self):
        _inheritance = {'base': [], 'second': ['base'],
                        'otherbase': [], 'first': ['otherbase']}
        _catch = 'base'
        _above = 'otherbase'
        _Expected = False
        _Actual = Exceptions.InConnection(_catch, _above, _inheritance)
        self.assertEqual(_Actual, _Expected)

    def test_InConnection_6(self):
        _inheritance = {'BaseException': [],
                        'Exception': ['BaseException'],
                        'LookupError': ['Exception'],
                        'KeyError': ['LookupError'],
                        }
        _catch = 'KeyError'
        _above = 'BaseException'
        _Expected = True
        _Actual = Exceptions.InConnection(_catch, _above, _inheritance)
        self.assertEqual(_Actual, _Expected)

    def test_getExtra_1(self):
        _inh = {'ArithmeticError': [], 'ZeroDivisionError': ['ArithmeticError']}
        _catches = ['ArithmeticError', 'ZeroDivisionError']
        _Expected = {'ArithmeticError': False, 'ZeroDivisionError': True}
        _Actual = Exceptions.getExtra(_inh, _catches)
        print("Actual: ", _Actual)
        self.assertDictEqual(_Actual, _Expected)

    def test_getExtra_2(self):
        _inh = {'base': [], 'second': ['base'],
                'otherbase': [], 'first': ['otherbase']}
        # _catches = ['base', 'otherbase', 'first', 'second']
        # _Expected =  {'base': False, 'otherbase': False, 'first': True, 'second': True}
        _catches = ['otherbase', 'first']
        _Expected = {'otherbase': False, 'first': True}
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
                       'otherbase',
                       'first : otherbase',
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

    def test_Find_4(self):
        _user_input = [6,
                       '10',
                       '11 : 10',
                       '12 : 11',
                       '20',
                       '13 : 11 20',
                       '21 : 20',
                       6,
                       '20',
                       '13',
                       '10',
                       '11',
                       '21',
                       '12', ]
        _Expected = ['13',
                     '11',
                     '21',
                     '12', ]
        _extra = {}
        with patch('builtins.input', side_effect=_user_input):
            _extra = Exceptions.Find()
        _Actual = Exceptions.RefineExtra(_extra)
        self.assertListEqual(_Actual, _Expected)

    def test_Find_5(self):
        _user_input = [4,
                       "winter",
                       "is",
                       "coming",
                       "OMG : winter is coming",
                       4,
                       "winter",
                       "is",
                       "coming",
                       "OMG"]
        _Expected = ['OMG']
        _extra = {}
        with patch('builtins.input', side_effect=_user_input):
            _extra = Exceptions.Find()
        _Actual = Exceptions.RefineExtra(_extra)
        self.assertListEqual(_Actual, _Expected)

    def test_Find_6(self):
        _user_input = [4,
                       "BaseException",
                       "Exception : BaseException",
                       "LookupError : Exception",
                       "KeyError : LookupError",
                       2,
                       "BaseException",
                       "KeyError"]
        _Expected = ['KeyError']
        _extra = {}
        with patch('builtins.input', side_effect=_user_input):
            _extra = Exceptions.Find()
        _Actual = Exceptions.RefineExtra(_extra)
        self.assertListEqual(_Actual, _Expected)

    def test_Find_7(self):
        _user_input = [14,
                       'a',
                       'b : a',
                       'c : a',
                       'f : a',
                       'd : c b',
                       'g : d f',
                       'i : g',
                       'm : i',
                       'n : i',
                       'z : i',
                       'e : m n',
                       'y : z',
                       'x : z',
                       'w : e y x',
                       2,
                       'm',
                       'm']
        _Expected = ['m']
        _extra = {}
        with patch('builtins.input', side_effect=_user_input):
            _extra = Exceptions.Find()
        _Actual = Exceptions.RefineExtra(_extra)
        self.assertListEqual(_Actual, _Expected)

    def test_Find_8(self):
        _user_input = [14,
                       'a',
                       'b : a',
                       'c : a',
                       'f : a',
                       'd : c b',
                       'g : d f',
                       'i : g',
                       'm : i',
                       'n : i',
                       'z : i',
                       'e : m n',
                       'y : z',
                       'x : z',
                       'w : e y x',
                       9,
                       'y',
                       'm',
                       'n',
                       'm',
                       'd',
                       'e',
                       'g',
                       'a',
                       'f']
        _Expected = ['m',
                     'e',
                     'g',
                     'f']
        _extra = {}
        with patch('builtins.input', side_effect=_user_input):
            _extra = Exceptions.Find()
        _Actual = Exceptions.RefineExtra(_extra)
        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
