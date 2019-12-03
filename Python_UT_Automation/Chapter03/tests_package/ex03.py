from dev_code.devlib01 import *
import unittest

mm = 0

def setUpModule():
    global mm
    mm = mymathlib()

def tearDownModule():
    global  mm
    del mm

class TestClass10(unittest.TestCase):

    @classmethod
    def SetUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_add(self):
        self.assertEqual(mm.add(2,3),5)

    def test_mul(self):
        self.assertEqual(mm.mul(2,3),6)

    def test_sub(self):
        self.assertEqual(mm.sub(2,3),-1)




