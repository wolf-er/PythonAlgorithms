'''3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.'''

num = int(input('Введите натуральное число '))
result = 0
while num > 0:
    result = result * 10 + num % 10
    num //= 10
print(result)