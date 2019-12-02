import unittest
import inspect

"""
Note that the test methods ran in alphabetical order, irrespective of the order of the
test methods in the code
"""

class TestCase01(unittest.TestCase):
    def test_003(self):
        self.assertEqual(True, True)
        print("Run : ", inspect.stack()[0][3])

    def test_001(self):
        self.assertAlmostEqual(3.55, 3.56, 1)
        print("Run : ", inspect.stack()[0][3])

    def test_005(self):
        self.assertAlmostEqual(3.55, 3.56, 1)
        print("Run : ", inspect.stack()[0][3])

    def test_002(self):
        self.assertAlmostEqual(3.55, 3.56, 1)
        print("Run : ", inspect.stack()[0][3])

""" 
    you can control VERBOSITY (0->2) from the code:
"""
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
