# Добавление пункта
products = ['tomatoes', 'cucumbers', 'apples', 'milk', 'tea']

products.append('meat')

print('Список после добавления пункта: ', products)

# Замена 2 пункта на новый
products_2 = ['tomatoes', 'cucumbers', 'apples', 'milk', 'tea']

products_2[1] = ('salad') 

print('Список после замены: ', products_2)

# Длина списка

products_3 = ['tomatoes', 'cucumbers', 'apples', 'milk', 'tea']

print('Длина списка: ', len(products_3))

# Сортировка списка по алфавиту

products_4 = ['tomatoes', 'cucumbers', 'apples', 'milk', 'tea']

products_4.sort(reverse=False)
print('Список после сортировки: ', products_4)

# Удаление последнего пункта

products_5 = ['tomatoes', 'cucumbers', 'apples', 'milk', 'tea']

products_5.pop(4)

print('Список после удаления последнего пункта: ', products_5)