import os
from os.path import join, dirname
from get_data import config

def generate_start():
    text_start = ['Обери команду\n' +
                  config['BUTTON1'] + '-' + config['DESCRIPTION1'] + '\n' +
                  config['BUTTON2'] + '-' + config['DESCRIPTION2'] + '\n' +
                  config['BUTTON3'] + '-' + config['DESCRIPTION3'] + '\n' +
                  config['BUTTON4'] + '-' + config['DESCRIPTION4']]
    separator = ', '
    text = separator.join(text_start)
    # print(text)

    return text


def generate_pay():
    text_pay = f"Справжні картки зі мною не працюють, гроші з вашого рахунку не будуть списані. Bикористовуйте цей номер тестової картки для оплати ваших продуктів: `{config['TEST_CARD_STRIPE']}`"

    return text_pay


def generate_terms():
    text = ['1.Платежі приймаються у формі кредитних/дебетових карток або цифрових гаманців.' + '\n' +
            '2.Замовлення будуть оброблені лише після отримання повної оплати.' + '\n' +
            '3.Відшкодування буде надано лише у випадку помилок у роботі обладнання.']
    separator = ', '
    text = separator.join(text)
    return text


def generate_help():
    text = f"Cлужба підтримки доступна за номером {config['SUPPORT']}"
    return text


def generate_inst():
    text = ['1.Обрати продукт з меню.' + '\n' +
            '2. Оплатити.' + '\n' +
            '3. Забрати товар або напій.']
    separator = ', '
    text = separator.join(text)
    return text


if __name__ == '__main__':
    # print(generate_inst())
    print(generate_start())
