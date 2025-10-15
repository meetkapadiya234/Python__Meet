import requests

data = requests.get("https://openweathermap.org/api?utm_source=chatgpt.com")
for i in data.json():
    print(i['city'])
