import requests
from bs4 import BeautifulSoup

class CurrencyConverter:
    def __init__(self, usd_rate):
        self.usd_rate = usd_rate

    def convert_to_usd(self, amount):
        return amount / self.usd_rate

    def convert_to_local_currency(self, amount):
        return amount * self.usd_rate

url = 'https://next.privat24.ua/exchange-rates'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    usd_rate = 36.43
    converter = CurrencyConverter(usd_rate)
    local_currency_amount = float(input("Введите сумму в вашей валюте: "))
    usd_amount = converter.convert_to_usd(local_currency_amount)

    print(f"{local_currency_amount} вашей валюты равно {usd_amount:.2f} долларов США")
else:
    print("Не удалось получить данные о курсах валют.")
