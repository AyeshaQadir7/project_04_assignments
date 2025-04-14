import requests
from pprint import pprint

API_Key = '8b9e9985a4a95c197a13c16ec88b05cd'

city = input('Enter a city: ')
base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
