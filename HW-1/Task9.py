'''9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).'''

a = float(input("Введите a "))
b = float(input("Введите b (не равное a) "))
c = float(input("Введите c (не равное a и b) "))

if (a < b and b < c or a > b and b > c):
    print('Среднее - ', b)
elif (b < a and a < c or b > a and a > c):
    print('Среднее - ', a)
elif (b < c and c < a or b > c and c > a):
    print('Среднее - ', c)