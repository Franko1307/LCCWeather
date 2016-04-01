from db import db_session
from models import Lectura
import requests

apikey = '9f7f4e7ce8bb9b072eba080ed7b9efd6'

params = {'q': 'Hermosillo', 'APPID': apikey}


def update():
    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params)
    json = r.json()

    print(json)

    l = Lectura(
        json['main']['temp'],
        json['main']['pressure'],
        json['main']['humidity']
    )
    db_session.add(l)

    db_session.commit()
