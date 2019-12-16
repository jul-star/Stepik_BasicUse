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
        # < a href = "https://stepic.org/media/attachments/lesson/24472/sample1.html" > 1 < / a >
        pattern = r"href\s*=\s*\"(.*?)\""
        _fa = re.findall(pattern, _txt)
        return _fa

    @staticmethod
    def LinkIsOnPage(_lnk, _txt):
        """
        match link in txt
        :param _lnk:
        :param _txt:
        :return: link is found in text
        """
        pattern = _lnk
        _match = re.search(pattern, _txt)
        if _match:
            return True
        else:
            return False

    @staticmethod
    def getInput():
        _url1 = input()
        _url1 = _url1.rstrip()
        _url2 = input()
        _url2 = _url2.rstrip()
        return [_url1, _url2]

    @staticmethod
    def twoSteps():
        (url1, url2) = Ex_3_4_06.getInput()
        page1Content = Ex_3_4_06.getPageContent(url1)
        hrefs1 = Ex_3_4_06.getListOfLinks(page1Content)
        for href in hrefs1:
            pageContent = Ex_3_4_06.getPageContent(href)
            if pageContent:
                if Ex_3_4_06.LinkIsOnPage(url2, pageContent):
                    return True
        return False

if __name__ == "__main__":
    found = Ex_3_4_06.twoSteps()
    if found:
        print('Yes')
    else:
        print('False')
