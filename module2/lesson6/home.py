import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(response.content, features="xml")

australian_dollar = soup.find("Valute", ID='R01010')

australian_nominal = australian_dollar.Nominal.text
australian_value = australian_dollar.Value.text
australian_name = australian_dollar.Name.text


print(f'({australian_nominal} шт.) {australian_name} стоит(ят) {australian_value} руб.')

usa_dollar = soup.find('Valute', ID='R01235')

usa_nominal = usa_dollar.Nominal.text
usa_value = usa_dollar.Value.text
usa_name = usa_dollar.Name.text

print(f'({usa_nominal} шт.) {usa_name} стоит(ят) {usa_value} руб.')

japan_yen = soup.find('Valute', ID='R01820')

japan_nominal = japan_yen.Nominal.text
japan_value = japan_yen.Value.text
japan_name = japan_yen.Name.text

print(f'({japan_nominal} шт.) {japan_name} стоит(ят) {japan_value} руб.')
