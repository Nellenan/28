import requests

response = requests.get('https://swapi.dev/api/starships/').json()
starships_api = response.get('results')

max_speed = 0
fastest_ship = ""

for ship in starships_api:
    speed = ship.get("max_atmosphering_speed")
    if speed == "n/a" or speed == '1000km':
        continue
    speed = int(speed)
    if speed > max_speed:
        max_speed = speed
        fastest_ship = ship.get("name")




print("The fastest ship is:", fastest_ship)

import requests


starships_list = []

response = requests.get('https://swapi.dev/api/starships/').json()
starships_api = response.get('results')

max_speed = 0
fastest_ship = ""

for ship in starships_api:
    speed = ship.get("max_atmosphering_speed")
    if speed == "n/a" or speed == '1000km':
        continue
    speed = int(speed)
    if speed > max_speed:
        max_speed = speed
        fastest_ship = ship.get("name")
        starships_list.append(fastest_ship)
    if len(starships_list) == 5:
        break