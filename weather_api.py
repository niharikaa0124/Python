import requests
from dotenv import load_dotenv
import os

load_dotenv()
city=input("Enter city :")
print(f"the city entered by the user is {city}")

api_key=os.getenv("WEATHER_API_KEY")

endpoint = "https://api.weatherapi.com/v1/current.json"

params={
    "key":api_key,
    "q":city,
}
try:
    response=requests.get(
        endpoint,
        params=params
    )
    data=response.json()
    # print(data)
    if response.status_code==200:
        cityy=data["location"]["name"]
        temp=data["current"]["temp_c"]
        condition=data["current"]["condition"]["text"]
        humidity=data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]
        feels_like=data["current"]["feelslike_c"]

        print(f"The city : {cityy} \nTemperature : {temp} \nCondition : {condition} \nHumidity : {humidity}\nWind Speed : {wind_speed}\nTemperature feels like : {feels_like} ")
    else:
        print(data["error"]["message"])
except Exception as e:
    print(e)