def type_logger(func):
    def wrapper(*args):
        str_tmp = ''
        lst_result = [f'{number}: {type(func(number))}' for number in args]
        lst_result.reverse()
        while len(lst_result) > 1:
           str_tmp += lst_result.pop() + ', '
        str_tmp += lst_result.pop()
        str_end = f'{func.__name__}({str_tmp})'
        return str_end

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3

print(calc_cube(5, 6))
