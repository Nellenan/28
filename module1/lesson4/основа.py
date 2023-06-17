# Первое задание

# favorite_actors = ['киану', 'скала']


# actor_in_film = input('Введите главного актёра в фильме: ').lower()
# rating = int(input('Введите рейтинг фильма: '))


# if actor_in_film.lower() in favorite_actors:
#     print('Рекомендую, потому что в нём играюе', favorite_actors)
# else:
#     print('Не рекомендую, потому что в нём не играет Киану')

# if actor_in_film in favorite_actors and rating >= 8:
#     print('Рекомендую')
# elif actor_in_film in favorite_actors or rating > 8:
#     print('Глянуть можно')
# else:
#     print('Фильм такой себе')




# Второе

import random

computer_number = random.randint(1, 10)
user_number = int(input('Угадайте число: '))

diffrence = abs(user_number - computer_number)

if computer_number == user_number:
    print('Поздравляем')
elif diffrence == 1:
    print('Почти угадал, число было', computer_number)
else:
    print('Попробуй ещё раз')