import requests

key = '9ed09ae29739c01a9cc51c596a1eb6ff'
city = 'Dubna,ru'
# city = input("City ?: ")
api_url = "http://api.openweathermap.org/data/2.5/weather?"
_params = {'q': city,
           'appid': key,
           'units':'metric'}
_response = requests.get(api_url, params=_params)
_status_code = _response.status_code
_content_type = _response.headers['Content-Type']
if _status_code == 200 and _content_type == 'application/json; charset=utf-8':
    data = _response.json()
    template = "Температура в {city} приблизительно {temperature}"
    print(template.format(city=city, temperature=data['main']['temp']))
else:
    print("Status code: ", _status_code)
