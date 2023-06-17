## 6 Специальная переменная __name__

# if __name__ == '_main_':
goods = [
    {
        'name': 'Iphone 7',
        'brand': 'Apple',
        'price': 100,

    },
    {
        'name': 'Ipad',
        'brand': 'Apple',
        'price': 50,
    },
    {
        'name': 'Windows Xp',
        'brand': 'Microsoft',
        'price': 150,
    }
]

    # 1 Лямбда
def on_price(item):
    return item['price']


print(sorted(goods, key=on_price))
print(sorted(goods, key=lambda item: item['price']))

    # 2 Функция filter


filtered_list = filter(lambda item: item['brand'] == 'Apple', goods)
filtered_list = list(filter(lambda item: item['brand'] == 'Apple', goods))
print(filtered_list)

    # 3 Функция map

numbers = ['1', '2', '3', '4', '5']
print(numbers)
result = list(map(int, numbers))
print(result)

names_list = ['Igor', 'Артём', 'Аня', 'Ксюша']
surnames = ['Иванов', 'Петрович', ' Максимов', 'Андреевна']
persons = list(map(lambda name, surname: f'{name} {surname}', names_list, surnames))
print(persons)

    # 4 Функция enumerate

new_goods = []

for index, item in enumerate(goods):
    print(index)
    new_goods.append({index: item})
print(new_goods)

    # 5 Функция zip

names_list = ['Igor', 'Артём', 'Аня', 'Ксюша']
surnames = ['Иванов', 'Петрович', ' Максимовна', 'Андреевна']

for name, surname in zip(names_list, surnames):
    print(name, surname)
# else:
#     print('Скрипт запустился извне')

