import unittest
import inspect
"""
Multiply Test Classes
"""
def setUpModule():
    """called once, before anything else in this module"""
    print("In setUpModule()...")
def tearDownModule():
    """called once, after everything else in this module"""
    print("In tearDownModule()...")

class TestClass04(unittest.TestCase):
 def test_case01(self):
    print("\nClassname : " + self.__class__.__name__)
    print("Running Test Method : " + inspect.stack()[0][3])

class TestClass05(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Set up class", cls.__class__.__name__)

    @classmethod
    def tearDownClass(cls):
        print("Tear down class", cls.__class__.__name__)

    def test_case01(self):
        print("\nClassname : " + self.__class__.__name__)
        print("Running Test Method : " + inspect.stack()[0][3])

if __name__ == '__main__':
    unittest.main(verbosity=0)
