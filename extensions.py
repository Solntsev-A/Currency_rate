import requests
import json
from config import keys

class APIException(Exception):
    pass

class Currency_rate:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось опознать валюту {quote}')

        try:
            keys[base]
        except KeyError:
            raise APIException(f'Не удалось опознать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/cf7ff297e67e0cf701930387/latest/{quote_ticker}')
        total_base = json.loads(r.content)['conversion_rates'][keys[base]]
        return round(total_base * amount, 2)