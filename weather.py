import requests
#import os
from datetime import datetime

api_key = '24aaaeec72b93fb7db4ec12ed33de0b6'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

file = open('weather.txt', 'w')

file.write ("-------------------------------------------------------------\n")
file.write ("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
file.write ("-------------------------------------------------------------\n")
file.write ("Current temperature is: {:.2f} deg C\n".format(temp_city))
file.write ("Current weather desc  :{}\n".format(weather_desc))
file.write ("Current Humidity      :{} %\n".format(hmdt))
file.write ("Current wind speed    :{} kmph".format(wind_spd))
file.close()