import requests

planets_list = []


response = requests.get('https://swapi.dev/api/')
planets_url = response.json()['planets']
response = requests.get(planets_url)


print(response.json())

for i in range(1, 6):
    detail_planet_url = f'{planets_url}{i}'
    response = requests.get(detail_planet_url)

    data = response.json()
    data['diameter'] = int(data['diameter'])

    planets_list.append(data)

max_diameter = 0
for planet in planets_list:
    if planet['diameter'] > max_diameter:
        max_diameter = planet['diameter']


for planet in planets_list:
    if max_diameter == planet['diameter']:
        print(planet)
        break


# print(max(planets_list, key=lambda x: x['diameter']))