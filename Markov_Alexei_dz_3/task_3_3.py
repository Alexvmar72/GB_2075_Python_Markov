def thesaurus(*args) -> dict:
    name_lst = args
    dict_out = {}
    for name in name_lst:
        key = name[0]
        if key not in dict_out:
            value = []
            value.append(name)
            dict_out[key] = value
        elif key in dict_out:
            key = name[0]
            dict_out.get(key).append(name)

    return dict_out


print(thesaurus("Иван", "Павел", "Мария", "Петр", "Илья", "Михаил"))

