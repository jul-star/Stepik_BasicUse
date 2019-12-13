import requests
import re


def get_response():
    global url, response
    url = r"https://docs.python.org/3.6/"
    response = requests.get(url)
    print('status_code: ', response.status_code)
    print('Content-Type: ', response.headers['Content-Type'])
    print('Header keys: ', response.headers.keys())
    print(type(response.headers))
    # print(responce.content)


def get_image():
    global url, response
    url = r"https://docs.python.org/3.6/_static/py.png"
    response = requests.get(url)
    with open("python_image.png", "wb") as f:
        f.write(response.content)


def get_search(_txt):
    global url, response
    url = r"https://yandex.ru/search/"
    params = {'text': _txt}
    response = requests.get(url, params)
    if response.status_code != 200:
        print("Error")
    return response.text


def about(_text, _str):
    pattern = r"<b>{0}</b>(.*?)<span".format(_text)
    _obj = re.findall(pattern, _str)
    print(type(_obj))
    if len(_obj) > 0:
        print(_text, ": ", _obj)
    else:
        print("Didn't find {0} in : ".format(_text))


# get_image()
# get_response()
text = "Stepik"
res = get_search(text)
about(text, res)
