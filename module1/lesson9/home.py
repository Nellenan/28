# 1

# import requests
# from bs4 import BeautifulSoup

# respons = requests.get('http://www.columbia.edu/~fdc/sample.html')
# soup = BeautifulSoup(respons.text, 'html.parser')
# contents = [h3.text for h3 in soup.findAll('h3')]
# print(contents)



# 2


import requests
from bs4 import BeautifulSoup

respons = requests.get('https://webscraper.io/test-sites/e-commerce/ajax/computers/tablets')
soup = BeautifulSoup(respons.text, 'html.parser')
items = soup.find_all(class_='row ecomerce-items ecomerce-items-ajax')
print(items)