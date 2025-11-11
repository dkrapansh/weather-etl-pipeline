import requests
from config import API_KEY

url = "https://api.openweathermap.org/data/2.5/weather"
params = {"q": "London", "appid": API_KEY, "units": "metric"}

r = requests.get(url, params=params)
print(r.status_code)
print(r.json())
