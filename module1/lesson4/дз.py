#Первое задание

# temperature = int(input('Сколько градусов на улице?: '))

# if temperature <= -30:
#     print('Очень холодно')
# elif temperature <= -15:
#     print('Холодно')
# elif temperature <= 0 :
#     print('Прохладно')
# elif temperature > 0 and temperature < 15:
#     print('Тепло')
# elif temperature >= 15 and temperature < 30:
#     print('Жарко')
# else:
#     print('Очень жарко')



#Второе задание

# import random

# print('Игра "Орёл или решка?"')
# print('1 = Орёл')
# print('2 = Решка')

# user_choice = int(input('Орёл или решка?: '))

# computer_choice = random.randint(1, 2)

# if user_choice == computer_choice:
#     print('Ты победил')
# else:
#     print('Ты проиграл')

#3

numbers = [1, 4, -3, 0, 10]
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # temp_value = numbers[i]
            # numbers[i] = numbers[j]
            # numbers[j] = temp_value

print(numbers) 
