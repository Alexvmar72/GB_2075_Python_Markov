def convert_name_extract(list_in: list) -> list:
    list_out = []
    name_greet = ''
    for work_name in list_in:
        work_name_list = work_name.split()
        name = work_name_list[-1]
        name = name.lower()
        name = name.capitalize()
        name_greet = 'Привет, ' + name + '!'

        list_out.append(name_greet)
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)

print(result)