'''Анализ. Определить, какое число в массиве встречается чаще всего.'''

import random

MASSIVE_LOW_BORDER = 0
MASSIVE_HIGH_BORDER = 20
MASSIVE_SIZE = 300

def dict_variant():
    mas = [random.randint(MASSIVE_LOW_BORDER,MASSIVE_HIGH_BORDER) for _ in range(MASSIVE_SIZE)]
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

'''Ожидаемая сложность O(n)
n = 10      100 loops, best of 3: 18.9 usec per loop
n = 100     100 loops, best of 3: 141 usec per loop
n = 200     100 loops, best of 3: 279 usec per loop
n = 300     100 loops, best of 3: 407 usec per loop
'''


def simple_variant():
    mas = [random.randint(MASSIVE_LOW_BORDER, MASSIVE_HIGH_BORDER) for _ in range(MASSIVE_SIZE)]
    max_elem = 0
    max_num = 0
    for elem in mas:
        num = 0
        for elem2 in mas:
            if elem2 == elem:
                num += 1
        if num > max_num:
            max_num = num
            max_elem = elem

'''Ожидаемая сложность O(n**2)
n = 10      100 loops, best of 3: 19.2 usec per loop
n = 100     100 loops, best of 3: 494 usec per loop
n = 200     100 loops, best of 3: 1.7 msec per loop
n = 300     100 loops, best of 3: 3.55 msec per loop
'''