'''2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.'''

import random

def sort_sli(mas):
    if len(mas) >= 2:
        middle = len(mas) // 2
        mas_left = sort_sli(mas[:middle])
        mas_right = sort_sli(mas[middle:])
        i, j = 0, 0
        new_mas = list()
        while i < len(mas_left) and j < len(mas_right):
            if mas_left[i] < mas_right[j]:
                new_mas.append(mas_left[i])
                i += 1
            else:
                new_mas.append(mas_right[j])
                j += 1
        if i == len(mas_left):
            new_mas = new_mas + mas_right[j:]
        else:
            new_mas = new_mas + mas_left[i:]
        return new_mas
    return mas

SIZE = 16
mas = [random.randint(0,50) for i in range(SIZE)]

#mas = [8,13,5,1,2,10,14,11,3,0,12,15,6,4,7,9]
print(mas)


new_mas = sort_sli(mas)
print(new_mas)
