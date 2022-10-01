import requests

city = "Moscow,RU"
appid = "e998ab55df0557a03123627cc3014494"


res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()


print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])

print("____________________________")

res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", i['main']['temp'],  "> \r\nПогодные условия <", i['weather'][0]['description'], ">")
    print("____________________________")
