import re
import requests


class Sites:
    @staticmethod
    def getFileContent(_fileName):
        _res = []
        with open(_fileName, "r") as f:
            line = f.readline()
            _res.append(line.rstrip())
            while line:
                line = f.readline()
                if line:
                    _res.append(line.rstrip())
        return _res

    @staticmethod
    def getUrls(_text):
        _res = []
        _pattern = r'href=[\'\"](.*?)[\'\"]' #\s{0,}>'
        _tmp = re.findall(_pattern, _text)
        if _tmp:
            for g in _tmp:
                _res.append(g)
        return _res

    @staticmethod
    def stripHttp(_raw):
        """
        http://, https:// ftp://
        :param _raw:
        :return:
        """
        _res = None
        _pattern = r'(http://|https://|ftp://)(.+)'
        _tmp = re.search(_pattern, _raw)
        if _tmp:
            _res = _tmp.group(2)
        else:
            _res = _raw
        return _res

    @staticmethod
    def skipRelative(_raw):
        """
        '../skip_relative_links'
        :param _raw:
        :return:
        """
        _res = None
        _pattern = r'^\.\.'
        _tmp = re.search(_pattern, _raw)
        if _tmp:
            return True
        else:
            return False

    @staticmethod
    def stripWww(_raw):
        """
        remove www.
        :param _raw:
        :return:
        """
        _res = None
        _pattern = r'(www\.)(.+)'
        _tmp = re.search(_pattern, _raw)
        if _tmp:
            _res = _tmp.group(2)
        else:
            _res = _raw
        return _res

    @staticmethod
    def stripPort(_raw):
        """
        remove :1345 from neerc.ifmo.ru:1345
        :param _raw:
        :return:
        """
        _res = None
        _pattern = r'(:\d+)'
        _res = re.sub(_pattern, '', _raw)
        return _res

    @staticmethod
    def stripPath(_raw):
        """
        remove everything after /
        :param _raw:
        :return:
        """
        _res = None
        _pattern = r'(.+)(/.*)'
        _res = re.sub(_pattern, r'\1', _raw)
        return _res

    @staticmethod
    def Strip(_content):
        """
        :param _content: text!!!!
        :return:
        """
        _res = []
        strips = ['stripHttp', 'stripPort', 'stripPath']  # , 'stripWww'
        c = globals()['Sites']
        for raw in _content:
            tmp = raw
            for strip in strips:
                func = getattr(c, strip)
                tmp = func(tmp)
            _res.append(tmp)
        return _res

    @staticmethod
    def getList(_fileName):
        _res = set()
        content = Sites.getFileContent(_fileName)
        _lst = Sites.Strip(content)
        _skip = Sites._skipRelativePath(_lst)
        for s in _skip:
            _res.add(s)
        _res = sorted(_res)
        return _res

    @staticmethod
    def _skipRelativePath(_lst):
        _res = []
        for _raw in _lst:
            if not Sites.skipRelative(_raw):
                _res.append(_raw)
        return _res

    @staticmethod
    def getContent():
        _url = input()
        print("Url: ", _url)
        _res = None
        _request = requests.get(url=_url)
        print("Status code: ", _request.status_code)
        if _request.status_code == 200:
            _res = _request.text
        return _res

    @staticmethod
    def Build():
        _res = set()
        _content = Sites.getContent()
        _urls = Sites.getUrls(_content)
        print(_urls)
        _lst = Sites.Strip(_urls)
        _skip = Sites._skipRelativePath(_lst)
        for s in _skip:
            _res.add(s)
        _res = sorted(_res)
        return _res


if __name__ == "__main__":
    print(Sites.Build())
