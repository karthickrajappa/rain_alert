import requests
import os
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
APPID = "55783735eb0a48e4282582719a5166cc"
MY_NUMBER = "+19896231871"

account_sid = "AC013411a00bd15f6828118bbf54105e1c"
auth_token = "886a642efa965ffdef17ae48f482b204"
os.environ.get()
params = {
    "lat": 9.175240,
    "lon": 76.503098,
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
        to='+919787456108'
    )

    print(message.status)
