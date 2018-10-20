'''2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.'''
from collections import Counter

class Tree():
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        if type(left) == str:
            self.left = Tree(left)
        else:
            self.left = left
        if type(right) == str:
            self.right = Tree(right)
        else:
            self.right = right

    def make_dict(self, path='', d = dict()):
        if self.left != None:
            self.left.make_dict(path + '0', d)
        if self.right != None:
            self.right.make_dict(path + '1', d)
        if self.value != None:
            d[self.value] = path

st = input('Введите строку для сжатия: ')
#st = 'beep boop beer!'
print('Бинарное несжатое представление:')
long_st = ' '.join(format(ord(x), 'b') for x in st)
print(long_st)

dest_old = Counter(st)
print(dest_old)
while len(dest_old) > 1:
    dest_new = dict()
    el1, el2, *other = sorted(dest_old, key = dest_old.get)
    for el in other:
        dest_new[el] = dest_old[el]
    dest_new[Tree(left = el1, right = el2)] = dest_old[el1] + dest_old[el2]
    dest_old = dest_new

d_res = dict()
list(dest_old.keys())[0].make_dict(d = d_res)
print(d_res)

short_st = ''
for el in st:
    short_st += d_res[el] + ' '
print('Бинарное сжатое представление:')
print(short_st.strip())


