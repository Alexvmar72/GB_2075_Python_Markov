from random import uniform

def transfer_list_in_str(list_in: list) -> str:
    price_str_sum = ' '
    for price in list_in:
        price = format(price, '.2f')
        price_str = str(price)
        price_str = price_str[:-3] + ' руб' + ' ' + price_str[-2:] + ' коп'
        price_str_sum += price_str + ',' + ' '



    str_out = price_str_sum
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in


print('Исходный список занимает место в области памяти: ', id(my_list))
result_2 = sort_prices(my_list)
print('После сортировки список занимает место в области памяти: ', id(my_list))
print(result_2)


def sort_price_adv(list_in: list) -> list:
    list_in.sort()
    list_out = [] + list_in
    list_out.reverse()
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    list_in.sort()
    list_out = list_in[-5:]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)