import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
APPID = "GET YOUR API"
MY_NUMBER = "YOUR NUMBER"

account_sid = "GET YOUR ID"
auth_token = "YOUR TOKEN"
os.environ.get()
params = {
    "lat": "YOUR LATITUDE",
    "lon": YOUR LONGITUDE,
    "exclude": "current,minutely,daily,alerts",
    "appid": APPID
}

response = requests.get(url=OWM_ENDPOINT, params=params)
weather_data = response.json()["hourly"]

hourly_weather = [weather_data[hour]["weather"][0]["id"] for hour in range(0, 12)]
is_rain = False
for i in hourly_weather:
    if i < 700:
        is_rain = True
if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Don't forget to bring and umbrella ☂️",
        from_=MY_NUMBER,
        to='TO NUMBER'
    )

    print(message.status)
