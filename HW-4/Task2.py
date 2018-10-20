'''2. Написать два алгоритма нахождения i-го по счёту простого числа.
Первый - использовать алгоритм решето Эратосфена.
Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.'''

'''Сложность простого алгоритма - O((n * ln(n))**2), т.к.
нам для нахождения n-ного простого придётся брать диапазон примерно в n * ln(n)
10      100 loops, best of 3: 34.1 usec per loop
50      100 loops, best of 3: 1.38 msec per loop
100     100 loops, best of 3: 7.34 msec per loop
200     100 loops, best of 3: 38.7 msec per loop
400     10 loops, best of 3: 197 msec per loop
'''
def base_simple_find(n):
    if n < 1:
        return 0
    if n == 1:
        return 2
    check_on_simpleness = 3
    num_simple = 1
    while num_simple < n:
        flag_simple = 1
        for j in range(2, int(check_on_simpleness / 2) + 1):
            if check_on_simpleness % j == 0:
                flag_simple = 0
        check_on_simpleness += 1
        if flag_simple:
            num_simple += 1
    return(check_on_simpleness-1)


#print(base_simple_find(500));

'''Сложность Эратосфена для вычисления простых чисел среди n = O(nlnln(n))
Значит сложность нашего алгоритма будет будет = O(n * ln(n) * lnln(n))
10      100 loops, best of 3: 14.8 usec per loop
50      100 loops, best of 3: 100 usec per loop
100     100 loops, best of 3: 167 usec per loop
200     100 loops, best of 3: 465 usec per loop
400     100 loops, best of 3: 980 usec per loop
'''
import math
def erato_simple_find(n):
    if n == 1:
        return 2
    if n == 2:
        return 3
    num = int(n * math.log(n) * 1.3)
    mas = [i for i in range(num)]

    for i in range(2, num):
        if mas[i]:
            j = i * 2
            while j < num:
                mas[j] = 0
                j += i
    result = [i for i in mas if i != 0]
    return result

print(erato_simple_find(3))