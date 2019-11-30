import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False, "test_something: Wrong assertion True==False")

    def test_2(self):
        self.assertAlmostEqual(1.E-10, 1.01E-10) #, 0.01, "test_2: Not Almost Equal")


if __name__ == '__main__':
    unittest.main()
