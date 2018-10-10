'''2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.'''
from collections import deque

def get_number(txt):
    while True:
        num = input("Введите {} неотрицательное шестнадцатиричное число ".format(txt))
        for elem in num:
            if elem not in ('1234567890ABCDEFabcdef'):
                print("Неверный формат числа")
                break
        else:
            return num

#на вебинаре сказали, что int пользоваться нельзя, но тут я его применяю для конвертации числа просто чтобы сократить число строк
def convert_hex_digit(st):
    if st.lower() == 'f':
        return 15
    elif st.lower() == 'e':
        return 14
    elif st.lower() == 'd':
        return 13
    elif st.lower() == 'c':
        return 12
    elif st.lower() == 'b':
        return 11
    elif st.lower() == 'a':
        return 10
    return int(st)

def convert_int_digit(num):
    if num == 10:
        return 'a'
    elif num == 11:
        return 'b'
    elif num == 12:
        return 'c'
    elif num == 13:
        return 'd'
    elif num == 14:
        return 'e'
    elif num == 15:
        return 'f'
    return str(num)

def sum_hex(num1, num2):
    sum_result = deque()
    addition = 0
    for i in range(max(len(num1), len(num2))):
        slag1, slag2 = 0, 0
        if len(num1) > i:
            slag1 = convert_hex_digit(num1[i])
        if len(num2) > i:
            slag2 = convert_hex_digit(num2[i])
        elem = (slag1 + slag2 + addition) % 16
        #print(slag1, slag2, addition)
        addition = (slag1 + slag2 + addition) // 16
        sum_result.appendleft(convert_int_digit(elem))
    if addition:
        sum_result.appendleft(convert_int_digit(addition))
    return sum_result

num1 = deque(get_number('первое'))
num2 = deque(get_number('второе'))
num1.reverse()
num2.reverse()
sum_result = sum_hex(num1, num2)
print("Сумма введенных чисел {}".format(''.join(sum_result)))

#тут следовало бы реализовать честное умножение в столбик первого числа на цифры второго, но не было времени, так что умножение я свел к цикличному суммированию первого числа
mlt_result = deque()
for n in num2:
    for i in range(convert_hex_digit(n)):
        mlt_result = sum_hex(mlt_result,num1)
        mlt_result.reverse()
    num1.appendleft('0')
mlt_result.reverse()
print("Произведение введенных чисел {}".format(''.join(mlt_result)))