def transform_string(numbers: int) -> str:

    if n % 10 == 0:
        return f'{n} процентов'
    elif n // 10 == 1:
        return f'{n} процентов'
    elif n % 10 == 1:
        return f'{n} процент'
    elif n % 10 <= 4:
        return f'{n} процента'
    elif n % 10 <= 9:
        return f'{n} процентов'


for n in range(1, 101):
    print(transform_string(n))
