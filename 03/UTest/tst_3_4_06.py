import unittest
from unittest.mock import patch
import containers
from ex_3_4_06 import *
# https://dev.to/vergeev/how-to-test-input-processing-in-python-3

class TestCase_3_4_06(unittest.TestCase):

    def test_getInput_1(self):

        user_input=[
            'https://stepik.org/lesson/24456/step/4?unit=6762',
            'https://my.dom.gosuslugi.ru/#!/no-privileges'
        ]
        Expected = [
            'https://stepik.org/lesson/24456/step/4?unit=6762',
            'https://my.dom.gosuslugi.ru/#!/no-privileges'
        ]
        u1 = ''
        u2 = ''
        with patch('builtins.input', side_effect=user_input):
            (u1,u2) = Ex_3_4_06.getInput()


        self.assertEqual(u1, Expected[0])
        self.assertEqual(u2, Expected[1])


if __name__ == '__main__':
    unittest.main()
