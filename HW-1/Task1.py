'''1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.'''
a = int(input ("Введите целое трехзначное число "))
x1 = a % 10
x2 = a // 10 % 10
x3 = a // 100
print ("Сумма цифр введенного числа: " + str(x1 + x2 + x3))
print ("Произведение цифр введенного числа: " + str(x1 * x2 * x3))