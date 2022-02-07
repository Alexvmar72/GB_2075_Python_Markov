def sum_list_1(dataset: list) -> int:
    sum_7 = 0
    for n in dataset:
        sum_1 = 0
        num_w = n
        while n != 0:
            dig_del = n % 10
            sum_1 += dig_del
            n = n // 10

        if sum_1 % 7 == 0:
            sum_7 = sum_7 + num_w
    return sum_7
#
def sum_list_2(dataset: list) -> int:
    sum_7 = 0
    for n in dataset:
        n += 17
        sum_1 = 0
        num_w = n
        while n != 0:
            dig_del = n % 10
            sum_1 += dig_del
            n = n // 10

        if sum_1 % 7 == 0:
            sum_7 = sum_7 + num_w

    return sum_7

my_list = []
for cub_number in range(1, 1000, 2):
    my_list.append(cub_number ** 3)

result_1 = sum_list_1(my_list)
print(result_1)

result_2 = sum_list_2(my_list)
print(result_2)
