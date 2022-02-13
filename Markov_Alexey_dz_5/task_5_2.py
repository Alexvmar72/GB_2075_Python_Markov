# (вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя
# ключевое cлово yield
from itertools import islice
n = int(input('Введите число для расчёта: '))

odd_nums = (num for num in range(1, n+1, 2))
print(type(odd_nums))

print(*islice(odd_nums, n))

print('Программа закончила свою работу')
