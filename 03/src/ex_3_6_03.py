import requests
import sys


def getInfo(_number):
    _api_url = 'http://numbersapi.com/{number}/math'
    _prms = {'json': 'true'}
    _url = _api_url.format(number=_number)
    _response = requests.get(_url, _prms)
    if _response.status_code == 200:
        data = _response.json()
        if data['found']:
            print('Interesting')
        else:
            print('Boring')


if __name__ == "__main__":
    for line in sys.stdin:
        line = line.rstrip()
        getInfo(line)
