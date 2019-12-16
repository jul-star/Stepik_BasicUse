import unittest
from unittest.mock import patch
from ex_3_4_06 import Ex_3_4_06


# https://dev.to/vergeev/how-to-test-input-processing-in-python-3

class TestCase_3_4_06(unittest.TestCase):

    def test_getInput_1(self):
        user_input = [
            'https://stepik.org/lesson/24456/step/4?unit=6762',
            'https://my.dom.gosuslugi.ru/#!/no-privileges'
        ]
        Expected = [
            'https://stepik.org/lesson/24456/step/4?unit=6762',
            'https://my.dom.gosuslugi.ru/#!/no-privileges'
        ]
        # u1 = ''
        # u2 = ''
        with patch('builtins.input', side_effect=user_input):
            (u1, u2) = Ex_3_4_06.getInput()

        self.assertEqual(u1, Expected[0])
        self.assertEqual(u2, Expected[1])

    def test_getPageContent_google(self):
        url = 'http://google.com'
        content = Ex_3_4_06.getPageContent(url)
        self.assertTrue(len(content) > 0)

    def test_getPageContent_1(self):
        url = 'https://stepic.org/media/attachments/lesson/24472/sample1.html'
        content = Ex_3_4_06.getPageContent(url)
        self.assertTrue(len(content) > 0)

    def test_getPageContent_2(self):
        url = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
        content = Ex_3_4_06.getPageContent(url)
        self.assertTrue(len(content) > 0)

    def test_getListOfLinks_1(self):
        content = r' ' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample1.html" > 1 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample2.html" > 2 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample3.html" > 3 < / a >'
        Actual = Ex_3_4_06.getListOfLinks(content)
        Expected = ['https://stepic.org/media/attachments/lesson/24472/sample1.html',
                    'https://stepic.org/media/attachments/lesson/24472/sample2.html',
                    'https://stepic.org/media/attachments/lesson/24472/sample3.html']
        self.assertListEqual(Actual, Expected)

    def test_getListOfLinks_2(self):
        content = r' ' \
                  r'< a href= "https://stepic.org/media/attachments/lesson/24472/sample1.html" > 1 < / a >' \
                  r'< a href ="https://stepic.org/media/attachments/lesson/24472/sample2.html" > 2 < / a >' \
                  r'< a href="https://stepic.org/media/attachments/lesson/24472/sample3.html" > 3 < / a >'
        Actual = Ex_3_4_06.getListOfLinks(content)
        Expected = ['https://stepic.org/media/attachments/lesson/24472/sample1.html',
                    'https://stepic.org/media/attachments/lesson/24472/sample2.html',
                    'https://stepic.org/media/attachments/lesson/24472/sample3.html']
        self.assertListEqual(Actual, Expected)

    def test_LinkIsOnPage_1(self):
        url = 'sample1.html'
        content = r' ' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample1.html" > 1 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample2.html" > 2 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample3.html" > 3 < / a >'
        Actual = Ex_3_4_06.LinkIsOnPage(url, content)
        Expected = True
        self.assertEqual(Actual, Expected)

    def test_LinkIsOnPage_2(self):
        url = 'sample4.html'
        content = r' ' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample1.html" > 1 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample2.html" > 2 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample3.html" > 3 < / a >'
        Actual = Ex_3_4_06.LinkIsOnPage(url, content)
        Expected = False
        self.assertEqual(Actual, Expected)

    def test_LinkIsOnPage_3(self):
        url = 'sample3.html'
        content = r' ' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample1.html" > 1 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample2.html" > 2 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample3.html" > 3 < / a >'
        Actual = Ex_3_4_06.LinkIsOnPage(url, content)
        Expected = True
        self.assertEqual(Actual, Expected)

    def test_LinkIsOnPage_4(self):
        url = 'https://stepic.org/media/attachments/lesson/24472/sample2.html'
        content = r' ' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample1.html" > 1 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample2.html" > 2 < / a >' \
                  r'< a href = "https://stepic.org/media/attachments/lesson/24472/sample3.html" > 3 < / a >'
        Actual = Ex_3_4_06.LinkIsOnPage(url, content)
        Expected = True
        self.assertEqual(Actual, Expected)

    def test_fail(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
