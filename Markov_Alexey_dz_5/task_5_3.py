tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А']

def check_gen(tutors: list, klasses: list):
    while len(tutors) > len(klasses):
        klasses.append('None')
    for name in range(0, len(tutors)):
        cort_class = (tutors[name], klasses[name])
        yield cort_class

generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator))

for _ in range(len(tutors)):
    print(next(generator))
#next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration