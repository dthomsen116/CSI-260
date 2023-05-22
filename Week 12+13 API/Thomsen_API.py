import requests
import json
from datetime import datetime


key = "fe821ad182651acfe879ff10b784ea0e"

url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter the city you'd like to see the weather for : ")

url_long = url + "appid=" + key + "&q=" + city_name

response = requests.get(url_long)

data = json.loads(response.text)

d = data


def weather_today(city_name):
    print()
    print('Current weather in %s:' % city_name)
    print(d['weather'][0]['main']), "\n",
    print()

    print('A more accurate description:'), "\n"
    print(print(d['weather'][0]['description']))
    print()

    print('Current temperature in %s:' % city_name)
    degrees_f_unrounded = ((((d['main']['temp']) - 273.15) * (9/5)) + 32)
    degrees_f = round(degrees_f_unrounded, 2)
    print(str(degrees_f) + " degrees fahrenheit")
    print()

    print('Feels Like:'), "\n"
    feels_like = ((((d['main']['feels_like']) - 273.15) * (9/5)) + 32)
    print(str(round(feels_like, 2)) + " degrees fahrenheit")
    print()

    print('Highs and lows:'), "\n"

    min_temp = (((d['main']['temp_min'] - 273.15) * (9/5)) + 32)
    max_temp = (((d['main']['temp_max'] - 273.15) * (9/5)) + 32)

    print("Minimum temperature of: " + (str(round(min_temp, 2))) + " degrees fahrenheit.")
    print("Maximum temperature: " + (str(round(max_temp, 2))) + " degrees fahrenheit.")
    print()

    print('Wind Speed: '), "\n"
    print(str((d['wind']['speed'])) + " Meters per second")
    print()

    print('Sunrise time: '), "\n"
    sun_rise =(d['sys']['sunrise'])
    print(datetime.utcfromtimestamp(sun_rise).strftime('%Y-%m-%d %H:%M:%S'))
    print()
    print('Sunset time: '), "\n"
    sun_set = (d['sys']['sunset'])
    print(datetime.utcfromtimestamp(sun_set).strftime('%Y-%m-%d %H:%M:%S'))
    print()

    choice = input("Would you like to look up another city? (y/n)")
    if choice == "y":
        weather_today(city_name=input("New City"))
    else:
        print("Have a good day!")


weather_today(city_name)
