'''3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.'''

import random

SIZE = 10

'''Идея - беру элемент собираю множества элементов меньше его и больше. В бОльшем по размеру множестве и будет лежать медиана.
Повторяю разбиение и поиск для него (с некоторыми поправками на размер множеств), в итоге получаю множество из одной медианы'''
def get_median(mas, num, lower=0):
    mas_lower = list()
    mas_upper = list()
    equal = 0
    for elem in mas:
        if elem < num:
            mas_lower.append(elem)
        elif elem > num:
            mas_upper.append(elem)
        else:
            equal += 1
    if lower + len(mas_lower) + equal > SIZE and lower + len(mas_lower) <= SIZE:
        return num
    elif lower + len(mas_lower) > SIZE:
        return get_median(mas_lower, mas_lower[0], lower)
    else:
        return get_median(mas_upper, mas_upper[0], lower + len(mas_lower) + 1)


mas = [random.randint(-100, 100) for i in range(2 * SIZE + 1)]
# mas = [56, -36, 65, -90, 73, -90, 47]

print('Массив ', mas)
print('Медиана через сортировку ', sorted(mas)[SIZE])
print('Медиана по алгоритму ', get_median(mas, mas[0]))
