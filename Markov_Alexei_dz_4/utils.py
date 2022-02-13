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
                value_lst = mean.split('Value>')
                value_1 = value_lst[-2]
                value_1_lst = value_1.split('<')
                value_2 = value_1_lst[0]
                value_2_lst = value_2.split(',')
                value = float(value_2_lst[0] + '.' + value_2_lst[-1])
                nominal_2_lst = mean.split('Nominal>')
                nominal_2 = nominal_2_lst[1]
                nominal_1_lst = nominal_2.split('<')
                nominal = int(nominal_1_lst[0])
                result_value = value / nominal

    return result_value

if __name__ == '__main__':
   print('Это модуль')
