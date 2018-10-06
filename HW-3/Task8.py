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
        result[row].append(input('Введите {} число {} строки '.format(col + 1, row + 1)))
        row_sum += float(result[row][col])
    result[row].append(str(row_sum))

for row in result:
    print('\t'.join(row))
