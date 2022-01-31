def convert_time(duration):
    days = duration // 86400
    hours = (duration // 3600) % 24
    minutes = (duration // 60) % 60
    seconds = duration % 60
    if days > 0:
        print(days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
    elif hours > 0:
        print(hours, 'час', minutes, 'мин', seconds, 'сек')
    elif minutes > 0:
        print(minutes, 'мин', seconds, 'сек')
    elif seconds > 0:
        print(seconds, 'сек')
#    return

duration = int(input('Введите время в секундах: '))

result = convert_time(duration)
#print(result)

