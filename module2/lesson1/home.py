# 1

# Сложение

try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
except ValueError:
    print('Введено некорректное число')
else:
    def summa(number_1, number_2):
        return number_1 + number_2

    result = summa(number_1, number_2)
    print(f'{number_1} + {number_2} = {result}')
finally:
    print('Программа суммы отработала')

# Вычитание

try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
except ValueError:
    print('Введено некорректное число')
else:
    def sub(number_1, number_2):
        return number_1 - number_2

    result = sub(number_1, number_2)
    print(f'{number_1} - {number_2} = {result}')
finally:
    print('Программа вычитания отработала')

# Умножение

try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
except ValueError:
    print('Введено некорректное число')
else:
    def multi(number_1, number_2):
        return number_1 * number_2

    result = multi(number_1, number_2)
    print(f'{number_1} * {number_2} = {result}')
finally:
    print('Программа умножения отработала')

# Деление

try:
    number_1 = int(input('Введите первое число: '))
    number_2 = int(input('Введите второе число: '))
except ValueError:
    print('Введено некорректное число')
else:
    def div(number_1, number_2):
        return number_1 / number_2

    result = div(number_1, number_2)
    print(f'{number_1} / {number_2} = {result}')
finally:
    print('Программа деления отработала')



# 2

try:
    a = int(input('Введите число а:'))
    b = int(input('Введите число b:'))
    c = int(input('Введите число c:'))
except ValueError:
    print('Введено неккоректное число')
else:
    def disc(a, b, c):
        return (b ** 2) - 4 * a * c

    result = disc(a, b, c)
    print(f'Дискриминант равен: {result}')
finally:
    print('Программа отработала')


# 3

import math

try:
    number = int(input('Введите положительное число: '))
except ValueError:
    print('Введено некорректное число')
else:
    def sqrt(number):
        return math.sqrt(number)

    result = sqrt(number)
    print(f'Квадратный корень из числа {number} равен: {result}')
finally:
    print('Программа отработала')
