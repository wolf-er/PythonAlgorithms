'''6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.'''

num = int(input('Введите номер буквы в алфавите (целое число от 1 до 26) '))

print('Это буква ' + chr(num - 1 + ord('a')))