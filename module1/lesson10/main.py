# 1



# summa = 10000
# init_summa = 0
# money_per_day = 1000
# days = 0



# while init_summa < summa:
#     init_summa += money_per_day
#     days += 1

# print('Чтобы накопить ' + str(summa) + ' нужно потратить ' + str(days) + ' дней')


# 2







# name = input('Ваше имя: ')
# debt = int(input('Ваша сумма долга: '))

# money_to_pay = 0

# while debt > money_to_pay:
#     money_to_pay = int(input('Введите сумму на погашение: '))
    
#     if money_to_pay >= debt:
#         print('Отлчино, не хотите взять ещё один кредит?')
#     else:
#         print('Маловато, ' + str(name) +  '. Нужно побольше')


# 3


# number = input('Введите число: ')
# print(len(number))


# number = int(input('Введите число: '))
# count = 0

# while number >0:
#     number //= 10
#     count += 1

# print(count)


# import requests
# from bs4 import BeautifulSoup
# import random

# key_word = input('Ключевое слово: <фест - выдать случайный фестиваль>, <хватит - закончить программу>')

# while key_word != 'хватит':
#     key_word = input('Ключевое слово: <фест - выдать случайный фестиваль>, <хватит - закончить программу>')
#     respons = requests.get('https://kudago.com/msk/festival/')
#     soup = BeautifulSoup(respons.text, 'html.parser')
#     fest = random.choice(soup.find_all(class_='post-title-link'))
#     print(fest['title'])
#     print(fest['href'])


# import time
# i = 1000

# while True:
#     print(i , '-' , 7 , '=' , i - 7 )
#     time.sleep(0.1)
#     i -= 7


# 4
from fpdf import FPDF

pdf = FPDF('P', 'cm', (10, 15))
pdf.add_page()


pdf.set_font('Arial', size=26)
pdf.set_text_color(255, 255, 255)
pdf.set_fill_color(255, 0, 0)
pdf.set_draw_color(0, 255, 0)
pdf.cell(w=10, h=5, txt='Hellow,World!', align='C', border=1, fill=True)

pdf.image('thumbnail.jpg', w=10, h=0, x=0, y=0)





pdf.output('test.pdf')










