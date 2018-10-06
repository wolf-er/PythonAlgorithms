'''7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.'''

import random

MASSIVE_LOW_BORDER = -100
MASSIVE_HIGH_BORDER = 100
MASSIVE_SIZE = 10

mas = [random.randint(MASSIVE_LOW_BORDER,MASSIVE_HIGH_BORDER) for _ in range(MASSIVE_SIZE)]
print(mas)

min1 = MASSIVE_HIGH_BORDER
min2 = MASSIVE_HIGH_BORDER

for elem in mas:
    if elem < min1:
        min2 = min1
        min1 = elem
    elif elem < min2:
        min2 = elem
print(min1,min2)