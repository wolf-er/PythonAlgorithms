import sys
def show_size(x, level = 0):
    result = 0
    print('\t' * level, 'type = {}, size = {}, object = {}'.format(x.__class__,sys.getsizeof(x),x))
    result += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for y in x.items():
                result += show_size(y, level + 1)

        elif not isinstance(x, str):
            for y in x:
                result += show_size(y, level + 1)
    return result

'''*********************************************************************************************'''
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

print('Total memory used in first task: ', show_size(MASSIVE_LOW_BORDER) + show_size(MASSIVE_HIGH_BORDER) + show_size(MASSIVE_SIZE) + show_size(mas) + show_size(mas_even) + show_size(i) + show_size(elem))
'''Вывод - использование памяти линейно по длине первого массива. Общая память получилась 956 байт при втором массиве из 8 элементов'''

'''*********************************************************************************************'''
'''8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
В конце следует вывести полученную матрицу.'''

NUM_COLS = 4
NUM_ROWS = 5
result = list()
for row in range(NUM_ROWS):
    row_sum = 0
    result.append(list())
    for col in range(NUM_COLS - 1):
        result[row].append(str(random.randint(0,100)))
        row_sum += float(result[row][col])
    result[row].append(str(row_sum))
print(result)
for row in result:
    print('\t'.join(row))

print('Total memory used in second task: ', show_size(NUM_COLS) + show_size(NUM_ROWS) + show_size(result) + show_size(row) + show_size(row_sum) + show_size(col))
'''Использованная память 2049 байт. Видно, что строковое хранение чисел - некруто, они весят по 50+ байт. Int же - по 28'''