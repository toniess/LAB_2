import requests

def getVisibility(n):

    return n['visibility']/1000


def getWind(n):
    return n['wind']['speed']

def printForecast(s):

    print(("Прогноз видимости (км)", "Прогноз скорости ветра (м/с)")[s == 'wind'])
    print('\t\t00:00\t03:00\t06:00\t09:00\t12:00\t15:00\t18:00\t21:00', end='')
    
    lastDate = ""
    
    for it in data['list']:
        date = it['dt_txt'].split(' ')[0]
        time = it['dt_txt'].split(' ')[1]
    
        hours = int(time.split(':')[0])
        
        if date != lastDate:
            print("")
            print(date, '\t', end='')
            
            if lastDate == "" :
                print('\t'*int(hours/3), end='')
                
            lastDate = date
        print((getVisibility(it), getWind(it))[s == 'wind'], '\t', end='') 
    
    
    print("")
    print("_________________________________________________________________________________")
    



city = "Moscow,RU"
appid = "e998ab55df0557a03123627cc3014494"


res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()


print("Город:", city)
print("Погода сегодня")
print("скорость ветра:", data['wind']['speed'], "м/с")
print("Видимость", data['visibility'], "м")


print("_________________________________________________________________________________")


res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()

printForecast('wind')
printForecast('visibility')
