import json

def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    with open(path_users_file, 'r', encoding='utf-8') as f1, open(path_hobby_file, 'r', encoding='utf-8') as f2:
        lst_users = []
        for str_users in f1:
            lst_users.append(str_users.replace(',', ' ').strip())

        lst_hobby = []
        for str_hobby in f2:
            lst_hobby.append(str_hobby.strip().split(','))

        if len(lst_users) < len(lst_hobby):
            return 1
        elif len(lst_users) > len(lst_hobby):
            lst_hobby.append(None)

        dict_tmp = dict(zip(lst_users, lst_hobby))

    return dict_tmp

dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)