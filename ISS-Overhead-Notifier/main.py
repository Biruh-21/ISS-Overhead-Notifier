import time

import requests
from datetime import datetime
import smtplib

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

def is_near():
    if (iss_longitude <= MY_LONG+5 or iss_longitude >= MY_LONG-5) and (iss_latitude <= MY_LAT+5 or iss_latitude >= MY_LAT-5):
        return True
    else:
        return False

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour

print(sunrise)
print(sunset)
print(time_now)


is_inrange = is_near()
my_email = "biruhtesfaye2121@gmail.com"
my_password = "izspftroghtydydi"

while True:
    time.sleep(60)
    if is_inrange and (time_now >= sunset or time_now <= sunrise):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="biruhtes@yahoo.com", msg="Subject:ISS-Overhead\n\nThe ISS is coming over your sky tonight!")




