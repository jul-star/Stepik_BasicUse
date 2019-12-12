import unittest
from ex_3_3_10 import *


class TestCase_3_3_10(unittest.TestCase):
    def test_tandemRepetitor_2(self):
        _lines = [
            "+ blabla is a tandem repetition",  # ['bla'] <_sre.SRE_Match object; span=(2, 8), match='blabla'>
            "+ 123123 is good too",  # ['123'] <_sre.SRE_Match object; span=(2, 8), match='123123'>
            "- go go",  # [] None
            "+ 22",  # ['2'] <_sre.SRE_Match object; span=(2, 4), match='22'>
            "- 333",  # [] None
            "+ 4444",  # ['44'] <_sre.SRE_Match object; span=(2, 6), match='4444'>
            "- 55555",  # [] None
            "+ 666666",  # ['666'] <_sre.SRE_Match object; span=(2, 8), match='666666'>
        ]
        _Actual = []
        _Expected = ["+ blabla is a tandem repetition",  # ['bla'] <_sre.SRE_Match object; span=(2, 8), match='blabla'>
                     "+ 123123 is good too",  # ['123'] <_sre.SRE_Match object; span=(2, 8), match='123123'>
                     "+ 22",  # ['2'] <_sre.SRE_Match object; span=(2, 4), match='22'>
                     "+ 4444",  # ['44'] <_sre.SRE_Match object; span=(2, 6), match='4444'>
                     "+ 666666",  # ['666'] <_sre.SRE_Match object; span=(2, 8), match='666666'>
                     ]
        for ln in _lines:
            if tandemRepetitor(ln):
                _Actual.append(ln)

        self.assertListEqual(_Actual, _Expected)


if __name__ == '__main__':
    unittest.main()
