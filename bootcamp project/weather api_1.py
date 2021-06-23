import requests
from datetime import datetime

api_key='3c5cce24263434e2ff1e10b1dc51e410'
location=input('Enter the city name: ')

complete_api_link="https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link=requests.get(complete_api_link)
api_data=api_link.json()

#Now, we declare the variables below

temp_city=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
hmdt=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
date_time=datetime.now().strftime("%d %b %y | %I:%M:%S %p")

file=open('info.txt',"a")
file.write(f"------------------------------------------------------\n")
file.write(f"weather stats for - {location.upper()} || {date_time}\n")
file.write(f"------------------------------------------------------\n")
file.write(f"Current temperature is: {round(temp_city,2)} deg C\n")
file.write(f"Current weather desc  :{weather_desc}\n")
file.write(f"Current humidity      :{hmdt} %\n")
file.write(f"Current wind speed    :{wind_spd} kmph\n")

#By this, we will have the output in a .txt file which gets saved in the existing folder
