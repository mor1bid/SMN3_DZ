# # a - открытие для добавления данных (из файла); r - открытие для чтения; w - открытие для записи данных
# # w+, r+
# # Словарь: setdefault добавление ключа, get - получение значения ключа
# from re import T
# from typing import Concatenate


# colors = ['red', 'blue', 'green']
# data = open('txt.txt', 'a')
# data.writelines(colors)
# data.write('\nКошмары\n')
# data.write('\nИнтернета\n')
# data.close()
# path = 'txt.txt'
# data = open(path, 'r')
# for line in data:
#     print(line, '\n')
# data.close()

# def new_string(symbol, count = 3):
#     return symbol * count
# print(new_string('!', 5))
# print(new_string('!'))
# print(new_string(5))

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w'))

# #РЕКУРСИЯ

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# List = []
# for i in range(1, 10):
#     List.append(fib(i))
# print(List)

# #Кортеж, неизменяемый список

# a = (3, 4)
# print(a[0], a[-1])

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))

# #Словарь

# dictionary = {}
# dictionary = \
#     {
#         'up': '^',
#         'left': '<',
#         'down': 'v',
#         'right': '>'
#     }
# print(dictionary)
# print(dictionary['left'])

# for k in dictionary.values():
#     print(k, end=' ')

# #множества

# colors = {'red', 'green', 'blue'}
# print(colors)
# colors.add('Sonic')
# print(colors)
# colors.discard('green')

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# u = a.union(b)
# i = a.intersection(b)
# dl = a.difference(b)
# dr = b.difference(a)
# q = a \
#     .union(b) \
#     .difference(a.intersection(b))
# s = frozenset(a)

# #Списки 2.0
# print()
# list1 = [1,2,3,4,5]
# list2 = list1
# list2[0] = 123
# for i in list1:
#     print(i, '\n')
# list1[1] = 123
# for i in list2:
#     print(i, '\n')

# print(len(list1))
# print('Эпизод:', list1.pop(2))
# print(list2)
# list2.append(11)
# list2.insert(1, 3)
# print(list1)

# R = int(input('Введите желаемое значение длины массива: '))
# kor = set()
# print('Заполните массив из', R, 'элементов:')
# for i in range(R):
#     num = int(input())
#     kor.add(num)
# rok = sorted(kor)
# print(rok)


strip = ["u", "ro", "bo", "rr", "ow", "s", "y", "u"]
res = 0
it = input('Введение искомое значение элемента: ')
for i in range(len(strip)):
    if strip[i] == it:
        res += 1
    if res == 2:
        print('Элемент ', it, 'найден на позиции', i)
        break
else:
    print('Данная позиция не найдена')

R = int(input('Введите желаемое значение длины массива: '))
List = []
print('Заполните массив из', R, 'элементов:')
for i in range(R):
    num = input()
    List.append(num)
print(List)
find = int(input('Введение искомый элемент: '))
for i in range(len(List)):
    if List[i].isdigit() and find==int(List[i]):
        print('Искомое число ', find, 'находится на', i, 'позиции')
        break
else:
    print('Данный элемент не найден в данном списке.')
