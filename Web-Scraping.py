from time import sleep
import requests
from bs4 import BeautifulSoup
from random import randint
import csv

payload = {'count': 12}
url = ('https://ge.oriflame.com/makeup/')

file = open('oriflame_catalogue.csv', 'w', encoding='utf-8')
file_ob = csv.writer(file)
file_ob.writerow(['დასახელება','ბრენდი','ფასი'])
while payload['count'] < 61:
    resp = requests.get(url, params=payload)
    print(url)
    content = resp.text
    soup = BeautifulSoup(content, 'html.parser')
    block = soup.find('section', class_='ui-product-list')
    block_all = block.find_all('a', class_="ui-product-box js-quick-shop")

    for each in block_all:
        title = each.find('span', class_='product-box-name js-cut-short').text
        brand = each.find('span', class_='product-box-brand').text
        price = each.find('span', class_='product-box-price').text
        price = price.strip()
        price = price.replace("GEL", "₾")
        file_ob.writerow([title, brand, price])
    payload['count'] += 12
    sleep(randint(7,10))

