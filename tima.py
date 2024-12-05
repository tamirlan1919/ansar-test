import requests
from bs4 import BeautifulSoup

url = 'https://www.cbr.ru/scripts/XML_daily.asp'

responce = requests.get(url)
soup = BeautifulSoup(responce.text, 'xml')

currencies_lst = ['USD', 'EUR', 'GBR', 'CHF', 'CNY']

for currency in soup.findAll('Valute'):
    if currency.CharCode.text in currencies_lst:
        print(f'{currency.CharCode.text}: {currency.Name.text} - курс {currency.Value.text}')
