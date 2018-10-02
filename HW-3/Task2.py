'''2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.'''

import random

MASSIVE_LOW_BORDER = 0
MASSIVE_HIGH_BORDER = 100
MASSIVE_SIZE = 10

mas = [random.randint(MASSIVE_LOW_BORDER,MASSIVE_HIGH_BORDER) for _ in range(MASSIVE_SIZE)]
print(mas)
mas_even = list()

for i, elem in enumerate(mas):
    if elem % 2 == 0:
        mas_even.append(i)
print(mas_even)
