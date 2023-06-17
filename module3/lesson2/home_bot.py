import vk_api
import random
import requests


token = 'vk1.a.ZD79SvplLFT6YRR2JGeNOJT4V6R1jyLgc1VqMFcUbfjUzdQ7cstsBgdwJVRPwGyeNsO7qFrZkt-twlizkOQDCNzz7lCORudfr0GHpqY8QJe0NgBZYeI-ajnvlvS2dwfENtFmY8jiK3vVXpGuGb9gA5n7CpPizKlDkAH1zhgSfSnnv2VPCKiaA-jc2s3MEZHRkWctHG6IzmBPSwgHJsICSw'

vk = vk_api.VkApi(token=token)


planets_list = []


response = requests.get('https://swapi.dev/api/')
planets_url = response.json()['planets']
response = requests.get(planets_url)


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
        print(planet['name'], planet['diameter'])
        break


response = requests.get("https://swapi.dev/api/")
starships_url = response.json()['starships']

response = requests.get(starships_url)


starships_list = []

for i in range(1, 6):
    detail_starships_url = f'{starships_url}{i}'
    response = requests.get(detail_starships_url)

    data = response.json()

    if response.status_code == 200:

        data['max_atmosphering_speed'] = int(data['max_atmosphering_speed'])

        starships_list.append(data)


print(max(starships_list, key=lambda x: x['max_atmosphering_speed']))


while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] > 0:
        message_text = messages['items'][0]['last_message']['text']

        if message_text == 'планеты':
            ans = f'Планета с максимальным диаметром - {planet["name"]}.' \
                  f' Диаметр составляет = {planet["diameter"]}'
        elif message_text == 'корабли':
            ans = f'Корабль с максимальной скоростью - {data["name"]}.' \
                  f' Его скорость составляет = {data["max_atmosphering_speed"]}'
        else:
            ans = 'Неизвестная команда'

        user_id = messages['items'][0]['last_message']['from_id']
        random_id = random.randint(-10 ** 7, 10 ** 7)

        vk.method('messages.send', {'user_id': user_id,
                                    'random_id': random_id,
                                    'message': ans
                                    })
