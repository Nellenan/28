# # 1 Способ
# def gen():
#     for i in range(1, 1001):
#         yield i ** 2
#
#
# for i in gen():
#     print(i)
#
# # 2  Способ
# squares = (n ** 2 for n in range(1, 1001))
#
# for square in squares:
#     print(square)



import requests
from bs4 import BeautifulSoup
from contextlib import contextmanager

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(response.content, features="xml")
currencies_list = soup.find_all("Valute")

@contextmanager
def get_course_info(currency):

     for currency in currencies_list:
         currency_nominal = currency.Nominal.text
         currency_value = currency.Value.text
         currency_name = currency.Name.text.lower()
         currency = f'({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} руб.'



with get_course_info('R01010') as currency:
    print(currency)