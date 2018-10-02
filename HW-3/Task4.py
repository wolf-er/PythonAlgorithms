'''4. Определить, какое число в массиве встречается чаще всего.'''

import random

MASSIVE_LOW_BORDER = 0
MASSIVE_HIGH_BORDER = 10
MASSIVE_SIZE = 10

mas = [random.randint(MASSIVE_LOW_BORDER,MASSIVE_HIGH_BORDER) for _ in range(MASSIVE_SIZE)]
print(mas)
d_res = dict()
for elem in mas:
    if elem not in d_res:
        d_res[elem] = 0
    d_res[elem] += 1

max_elem, max_entry = 0, 0
for elem in d_res:
    if d_res[elem] > max_entry:
        max_entry = d_res[elem]
        max_elem = elem

print('Чаще всего встречается число {}. Количество вхождений в массив - {}'.format(max_elem, max_entry))