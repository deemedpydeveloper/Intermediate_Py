# Comparing Sunrise and Sunset with Current Time.

import requests
import datetime as dt

MY_LAT = 17.968901
MY_LONG = 79.594055

parameters = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = dt.datetime.now()
print(time_now.hour)