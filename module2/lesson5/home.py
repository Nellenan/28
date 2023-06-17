import requests


starships_list = []

response = requests.get('https://swapi.dev/api/starships/').json()
starships_api = response.get('results')

max_speed = 0
fastest_ships = ""

for ships in starships_api:
    speed = ships.get("max_atmosphering_speed")
    if speed == "n/a" or speed == '1000km':
        continue
    speed = int(speed)
    if speed > max_speed:
        max_speed = speed
        fastest_ships = ships.get("name")
        starships_list.append(fastest_ships)
    if len(starships_list) == 5:
        break

print(starships_list)

