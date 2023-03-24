def transform_string(numbers: int) -> str:

    if numbers % 10 == 0:
        result = f'{numbers} процентов'
    elif numbers // 10 == 1:
        result = f'{numbers} процентов'
    elif numbers % 10 == 1:
        result = f'{numbers} процент'
    elif numbers % 10 <= 4:
        result = f'{numbers} процента'
    elif numbers % 10 <= 9:
        result = f'{numbers} процентов'
    return result


for n in range(1, 101):
    print(transform_string(n))
