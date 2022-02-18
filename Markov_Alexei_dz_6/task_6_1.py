from pprint import pprint

def get_parse_attrs(line: str) -> tuple:
    value_lst = line.split('- -')
    remote_addr = value_lst[0]
    value_1_lst = line.split('"')
    value_2_lst = value_1_lst[1]
    value_3_lst = value_2_lst.split(' /')
    request_type = value_3_lst[0]
    value_4_lst = value_2_lst.split(' ')
    requested_resource = value_4_lst[1]
    return remote_addr, request_type, requested_resource

lst_out = list()

with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        lst_out.extend([get_parse_attrs(line)]) #каждый раз удивляюсь, насколько этот язык проще, чем мои мысли.

pprint(lst_out)