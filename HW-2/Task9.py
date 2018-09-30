'''9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.'''

sum = 0
elem = 0
while True:
    num = int(input('Введите натуральное число или 0 для завершения '))
    if num == 0:
        break
    elemPart = num
    sPart = 0
    while num > 0:
        sPart += num % 10
        num //= 10
    if sPart > sum:
        sum = sPart
        elem = elemPart
print("Максимальная сумма цифр у числа {} - {}".format(elem, sum))