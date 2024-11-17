import requests
import json


def get_min_am():
    url = 'https://core.telegram.org/bots/payments/currencies.json'
    response = requests.get(url)
    data = json.loads(response.text)

    min_amount = data['UAH']['min_amount']
    print(f"The minimum amount for UAH is: {min_amount}")
    return min_amount
