import requests

response = requests.get("https://swapi.dev/api/")
starships_url = response.json()['starships']

response = requests.get(starships_url)
print(response.json())

starships_list = []

for i in range(1, 6):
    detail_starships_url = f'{starships_url}{i}'
    response = requests.get(detail_starships_url)

    data = response.json()

    if response.status_code == 200:

        data['max_atmosphering_speed'] = int(data['max_atmosphering_speed'])

        starships_list.append(data)

print(starships_list)

print(max(starships_list, key=lambda x: x['max_atmosphering_speed']))
