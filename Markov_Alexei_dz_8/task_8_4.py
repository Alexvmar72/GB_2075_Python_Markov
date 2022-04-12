from functools import wraps

def val_checker(func):
    def checker(func_in):
        @wraps(func_in)
        def wrapper(number):
            if type(number) == int and func(number) > 0:
                result = func_in(number)
            else:
                raise ValueError (f'wrong val {number}')
            return result
        return wrapper
    return checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube(-5))