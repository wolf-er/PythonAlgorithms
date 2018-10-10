'''1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.'''


from collections import Counter

def data_collector():
    result = Counter()
    total = 0
    num = int(input("Сколько предприятий? "))
    for n in range(num):
        name = input("Введите название {}/{} предприятия ".format(n+1, num))
        for i in range(4):
            profit = int(input("Введите прибыль за {} квартал ".format(i+1)))
            result[name] += profit
            total += profit
    return total,result

total, data = data_collector()
#data = {'Number-1': 100, 'Second': 200, 'Third': 300, 'Last': 600}
#total = 1200


mean = total / len(data)
print('Средняя прибыль за год ', mean)
print('Ниже среднего годовая прибыль у: ')
for firm in data:
    if data[firm] < mean:
        print(firm, data[firm])

print('Выше среднего годовая прибыль у: ')
for firm in data:
    if data[firm] > mean:
        print(firm, data[firm])