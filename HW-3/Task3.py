'''3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.'''

import random

MASSIVE_LOW_BORDER = 0
MASSIVE_HIGH_BORDER = 100
MASSIVE_SIZE = 10

mas = [random.randint(MASSIVE_LOW_BORDER,MASSIVE_HIGH_BORDER) for _ in range(MASSIVE_SIZE)]
print(mas)

max_num, max_index = MASSIVE_LOW_BORDER, 0
min_num, min_index = MASSIVE_HIGH_BORDER, 0

for i, elem in enumerate(mas):
    if elem > max_num:
        max_num = elem
        max_index = i
    if elem < min_num:
        min_num = elem
        min_index = i
mas[max_index] += mas[min_index]
mas[min_index] = mas[max_index] - mas[min_index]
mas[max_index] -= mas[min_index]
print(mas)
