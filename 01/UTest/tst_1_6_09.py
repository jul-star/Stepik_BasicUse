import unittest
from ex_1_6_09 import LoggableList

class TestCase_LoggableList(unittest.TestCase):
    def test_append(self):
        l = LoggableList()
        l.extend([1,2,3])
        val = 4
        l.append(val)
        Expected = [1,2,3,val]
        self.assertListEqual(l, Expected)
        self.assertEqual(l.getVal(), val)

if __name__ == '__main__':
    unittest.main()
