number = int(input('Введите номер координатной четверти от 1 до 4: '))

if number == 1:
    print('Диапазон возможных координат четверти', number,': x>0, y>0')
elif number == 2:
    print('Диапазон возможных координат четверти', number,': x<0, y>0')
elif number == 3:
    print('Диапазон возможных координат четверти', number,': x<0, y<0')
elif number == 4:
    print('Диапазон возможных координат четверти', number,': x>0, y<0')
elif number > 4 or number < 1:
    print('Такой четверти не существует')