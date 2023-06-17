import random
import requests
from bs4 import BeautifulSoup


# respons = requests.get('https://i-fakt.ru')
# soup = BeautifulSoup(respons.text,'html.parser')
# facts = soup.find_all(class_='p-2 clearfix')
# random_fact = random.choice(facts)
# print(random_fact.h4.text)
# print(random_fact.a['href'])

# for i_fact in facts:
#     print(i_fact.h4.text)
#     print(i_fact.a['href'])
#     print('-' * 100)




# p-2 clearfix


respons = requests.get('https://kudago.com/msk/festival/')
soup = BeautifulSoup(respons.text, 'html.parser')
fest = random.choice(soup.find_all(class_='post-title-link'))
print(fest['title'])
print(fest['href'])



# post title link























