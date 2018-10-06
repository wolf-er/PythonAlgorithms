'''6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.'''

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

final_sum = 0
if min_index < max_index:
    my_iterator = range(min_index + 1, max_index)
else:
    my_iterator = range(max_index + 1, min_index)
for i in my_iterator:
    final_sum += mas[i]

print('Сумма элементов между минимумом и максимумом {}'.format(final_sum))