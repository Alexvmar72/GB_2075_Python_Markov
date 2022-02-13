def get_numbers(src: list):
    for num in range(1, len(src)):
        if src[num] > src[num - 1]:
            yield src[num]

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))