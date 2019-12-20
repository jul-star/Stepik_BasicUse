import unittest
from ex_1_6_08 import ExtendedStack


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self._lst = ExtendedStack()
        self._lst.extend([1, 2, 3])

    def test_sum(self):
        Actual = self._lst.sum()
        Expected = 2 + 3
        self.assertEqual(Actual, Expected)
        ExpectedList = [1, Expected]
        self.assertListEqual(self._lst, ExpectedList)

    def test_sub(self):
        Actual = self._lst.sub()
        Expected = 3 - 2
        self.assertEqual(Actual, Expected)
        ExpectedList = [1, Expected]
        self.assertListEqual(self._lst, ExpectedList)

    def test_mul(self):
        Actual = self._lst.mul()
        Expected = 3*2
        self.assertEqual(Actual, Expected)
        ExpectedList = [1, Expected]
        self.assertListEqual(self._lst, ExpectedList)

    def test_div(self):
        Actual = self._lst.div()
        Expected = 3 // 2
        self.assertEqual(Actual, Expected)
        ExpectedList = [1, Expected]
        self.assertListEqual(self._lst, ExpectedList)


if __name__ == '__main__':
    unittest.main()
