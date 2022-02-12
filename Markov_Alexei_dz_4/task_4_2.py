#В корневой директории урока создать task_4_2.py и написать в нём функцию currency_rates(),
# принимающую в качестве аргумента код валюты (например, USD, EUR, SGD, ...)
# и возвращающую курс этой валюты по отношению к рублю.
#
#Использовать библиотеку requests.
#
#В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
#
#Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
#
#Можно ли, используя только методы класса str, решить поставленную задачу?
#Функция должна возвращать результат числового типа, например float.
#Подумайте:
#
#есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
#Сильно ли усложняется код функции при этом?
#Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
#
#Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
#В качестве примера выведите курсы доллара и евро.
#
#ВНИМАНИЕ! Используйте стартовый код для своей реализации:

import requests

def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    code = code.upper()
    api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(api_url)
    data_str = response.text
    if code not in data_str or len(code) > 3:
        result_value = None
    else:
        data_list = data_str.split('Valute ID')
        for mean in data_list:
            if code in mean:
                rate = mean[-25:-18]
                result_value = rate







        #print(data_list)
      ## здесь должно оказаться результирующее значение float
    return result_value

print(currency_rates("USD"))
print(currency_rates("noname"))