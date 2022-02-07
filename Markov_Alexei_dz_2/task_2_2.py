def convert_list_in_str(list_in: list) -> str:
    str_out = ' '
    for idx, word in enumerate(list_in):
        if word.isdigit() and len(word) == 1:
            word = '"' + '0' + word[-1] + '"'
            list_in[idx] = word
        elif word.isdigit():
            word = '"' + word + '"'
            list_in[idx] = word
        elif '+' in word and len(word) > 1 and len(word) < 3:
            word = '"' + word[0] + '0' + word[-1] + '"'
            list_in[idx] = word
        elif '-' in word and len(word) > 1 and len(word) < 3:
            word = '"' + word[0] + '0' + word[-1] + '"'
            list_in[idx] = word
        elif '-' in word and len(word) >= 3:
            word = '"' + word + '"'
            list_in[idx] = word
        elif '+' in word and len(word) >= 3:
            word = '"' + word + '"'
            list_in[idx] = word



        str_out += word + ' '
    return str_out


my_list = ['в', '5', 'часов', '07', 'минут', 'температура', 'воздуха', 'была', '+17', 'градусов']

result = convert_list_in_str(my_list)
print(result)