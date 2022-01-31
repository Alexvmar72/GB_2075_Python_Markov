def convert_time(duration):
    days = duration // 86400
    hours = (duration // 3600) % 24
    minutes = (duration // 60) % 60
    seconds = duration % 60
    if days > 0:
        return (days, 'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
    elif hours > 0:
        return (hours, 'час', minutes, 'мин', seconds, 'сек')
    elif minutes > 0:
        return (minutes, 'мин', seconds, 'сек')
    elif seconds > 0:
        return (seconds, 'сек')

duration = int(input('Введите время в секундах: '))

result = convert_time(duration)
print(result)

