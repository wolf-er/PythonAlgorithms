'''5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.'''

st = ''
for i in range(32,127):
    st += '{}:"{}", '.format(i, chr(i))
    if i % 10 == 1:
        print(st)
        st = ''
st += '{}:"{}"'.format(127, chr(127))
print(st)