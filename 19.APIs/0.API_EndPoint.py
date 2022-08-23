# API ---> Application Programming Interface.
## It serves as a mediator for the programmer to access the data of a website by the set of rules.
## Mostly used by the programmers to create a software or establish a connection with existing system.

# API EndPoint --> It is the URL, which holds the data, generally in JSON Format.
## It is used to access data officially.

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

# Status Codes ---> These are the codes which tells the user about the condition of establishment of request to the current webpage.
## 1xx informational response – ongoing process.
## 2xx successful – successful establishment.
## 3xx redirection – more actions required.
## 4xx client error – syntax error at client side.
## 5xx server error – bad condition at server side.


# Tapping into API data.
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

location = (longitude, latitude)
print(location)