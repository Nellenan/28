# numbers = []
# for i in range(101):
#     numbers.append(i)
# print(numbers)


import random

animals = []
animals_descripshons = []

for i in range(3):
    animal = input('Введите название животного: ')
    descripshion = input('Введите описание животного: ')

animals.append(animal)
animals_descripshons.appendp(descripshion)

for i in range(3):
    random_animal = random.choice(animals)
    random_description = random.choice(animals_descripshons)

print(animal, animals_descripshons)


# from random import randint
# numbers = [randint(0, 5) for _ in range(30)]
# print(('Кол-во 5: '), numbers.count(5))
# print(('Список чисел: '), numbers)