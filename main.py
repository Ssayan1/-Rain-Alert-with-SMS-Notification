
import os
import requests

from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = os.environ.get("TWILIO_SID")

auth_token = os.environ.get("AUTH_TOKEN")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast/"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": 26.388130,
    "lon": 90.020149,
    "appid": api_key,
    "cnt": 4
}
response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"][0])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(account_sid,auth_token,  http_client=proxy_client)
    message = client.messages.create(
        body="it's raining ! bring an umbrella",
        from_="+1 218 306 9822",
        to="+919382886797",
    )
print(message.status)
