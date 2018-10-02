'''5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.'''

import random

MASSIVE_LOW_BORDER = -100
MASSIVE_HIGH_BORDER = 100
MASSIVE_SIZE = 10

mas = [random.randint(MASSIVE_LOW_BORDER,MASSIVE_HIGH_BORDER) for _ in range(MASSIVE_SIZE)]
print(mas)

max_elem, max_index = MASSIVE_LOW_BORDER, 0
for i, elem in enumerate(mas):
    if elem < 0 and elem > max_elem:
        max_elem = elem
        max_index = i
print('Максимальный отрицательный элемент {}. Его индекс {}'.format(max_elem, max_index))