from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count: int) -> list:
    list_out = []          #создал пустой список
    while count != 0:      #создал цикл и условие для его окончания
        get_jok = str(choice(nouns) + ' ' + choice(adverbs) + ' '+ choice(adjectives)) # собираю строку с шуткой
        list_out.append(get_jok) #добавляю строку в список
        count -= 1  #уменьшаю счётчик на единицу

    return list_out


print(get_jokes(2))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий: документирование, флаг и именованные аргументы
#def get_jokes_adv(...) -> list:
#     # пишите реализацию здесь
#    return []