import requests
import re


class Ex_3_4_06:
    @staticmethod
    def getPageContent(_url):
        """
        get content by url
        :param _url:
        :return: content
        """
        _response = requests.get(_url)
        if _response.status_code == 200:
            return _response.text
        return None

    @staticmethod
    def getListOfLinks(_txt):
        """
        find all href in document
        :param _txt:
        :return: list of matches
        """
        pattern = r"href=(.*?)"
        _fa = re.findall(pattern, _txt)
        if _fa is not None:
            return _fa.groups()
        return None

    @staticmethod
    def LinkIsOnPage(_lnk, _txt):
        """
        match link in txt
        :param _lnk:
        :param _txt:
        :return: link is found in text
        """
        pattern = r"{0}".format(_lnk)
        _match = re.match(pattern, _txt)
        if _match is not None:
            return True
        else:
            return False

    @staticmethod
    def getInput():
        url1 = input()
        url1 = url1.rstrip()
        url2 = input()
        url2 = url2.rstrip()
        return [url1, url2]


if __name__ == "__main__":
    url1, url2 = Ex_3_4_06.getInput()
    page1Content = Ex_3_4_06.getPageContent(url1)
    hrefs1 = Ex_3_4_06.getListOfLinks(page1Content)
    for href in hrefs1:
        pageContent = Ex_3_4_06.getPageContent(href)
        if Ex_3_4_06.LinkIsOnPage(url2, pageContent):
            print('Yes')
    print('False')
