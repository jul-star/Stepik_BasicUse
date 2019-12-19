import requests
import json
from os import path


class Artists:
    @staticmethod
    def getInfo(_id):
        client_id = '202aa3448102e04e9318'
        client_secret = '4f9c9ba4dd5b6d6f88544f24aec787da'

        # инициируем запрос на получение токена
        r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                          data={
                              "client_id": client_id,
                              "client_secret": client_secret
                          })
        r.encoding = 'utf-8'  # ЭТО ОЧЕНЬ ВАЖНОЕ ДОПОЛНЕНИЕ !!!
        # разбираем ответ сервера
        j = json.loads(r.text)

        # достаем токен
        token = j["token"]

        # создаем заголовок, содержащий наш токен
        headers = {"X-Xapp-Token": token}
        # инициируем запрос с заголовком
        _url = 'https://api.artsy.net/api/artists/{id}'
        _api_url = _url.format(id=_id)
        r = requests.get(_api_url, headers=headers)

        # разбираем ответ сервера
        j = json.loads(r.text)
        # print(j)
        _name = j['sortable_name']
        _birthday = j['birthday']
        return [_name, _birthday]

    @staticmethod
    def getArtistIds(_fn):
        _path = '../data/{file}'
        _res = []
        _full_path = _path.format(file=_fn)
        if path.isfile(_full_path):
            with open(_full_path, "r") as f:
                line = f.readline()
                if line:
                    line = line.rstrip()
                    _res.append(line)
                while line:
                    line = f.readline()
                    if line:
                        line = line.rstrip()
                        _res.append(line)
        else:
            print("Can't open file: ", _full_path)
        return _res

    @staticmethod
    def run():
        _file_name = 'ex_3_6_04_Artist_ids.txt'
        _ids = Artists.getArtistIds(_file_name)
        if not _ids:
            return
        # print("Ids: ", _ids)
        _tmp = {}
        for _id in _ids:
            _name, _birthday = Artists.getInfo(_id)
            _tmp[_name] = _birthday

        _res = sorted(_tmp.items(), key=lambda x: x[1])
        # print(_res)
        Artists.printArtistNames(_res)

    @staticmethod
    def printArtistNames(_res):
        for _name, _birthday in _res:
            print(_name)


if __name__ == "__main__":
    Artists.run()
