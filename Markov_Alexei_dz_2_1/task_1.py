day = int(input('Введите день недели: '))

if day >= 1 and day <= 7:
    if day >= 1 and day <= 5:
        print(day, 'день не является выходным')
    else:
        print(day, 'день является выходным')
else:
    print('Введите корректное число дня недели')
