# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
# :6^6^6^6^6^6v
# -(x or y or z) = (-x) and (-y) and (-z)
# x   y   z
# 0   0   0
# 0   0   1
# 0   1   0
# 1   0   0
# 0   1   1
# 1   1   0
# 1   1   1

x = y = z = 0

while x <=1:
    while y <= 1:
        while z <=1:
            print(x, y, z)
            if (not (x or y or z)) == ((not x) and (not y) and (not x)):
                print('Выражение истинно')
            else:
                print('Выражение ложно')
            z += 1
        z = 0
        y += 1
    z = 0
    y = 0
    x += 1
