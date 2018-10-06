'''9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.'''
import random

MASSIVE_LOW_BORDER = -100
MASSIVE_HIGH_BORDER = 100
NUM_COLS = 5
NUM_ROWS = 2

result = [[str(random.randint(MASSIVE_LOW_BORDER,MASSIVE_HIGH_BORDER)) for _ in range(NUM_COLS)] for __ in range(NUM_ROWS)]

for row in result:
    print('\t'.join(row))

max_elem = MASSIVE_LOW_BORDER
for col in range(NUM_COLS):
    min_elem = MASSIVE_HIGH_BORDER
    for row in range(NUM_ROWS):
        if int(result[row][col]) < min_elem:
            min_elem = int(result[row][col])
    if max_elem < min_elem:
        max_elem = min_elem
    # print(min_elem)
print('Максимальный элемент среди минимальных по столбцам {}'.format(max_elem))
