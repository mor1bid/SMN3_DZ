# si = int(input('1. Задайте длину списка: '))
# ray = []
# res = 0
# print('Введите', si, 'элемента(-ов) списка:')
# for i in range(si):
#     num = int(input())
#     ray.append(num)
# print(ray)
# for i in range(si):
#     if i%2!=0:
#         res += ray[i]
# print('Сумма элементов на нечётных позициях в данном списке =', res)

# i2 = 0
# ar = []
# print('2. Произведение пар элементов в данном списке =', end=' ')
# for i in range(si):
#     if i<si/2:
#         i2-=1
#         res= ray[i]*ray[i2]
#         ar.append(res)
# print(ar)

# import random
# strip = []
# for i in range(si):
#     num = round(random.uniform(-10.1, 10.1), 2)
#     strip.append(num)
# big = strip[0]
# tin = strip[0]
# print('3.', strip, '\n' 'Разность между максимальным и минимальным значениями данного списка =', end=' ')
# for i in strip:
#     if i%1>=big%1:
#         big=i
#     elif i%1<=tin%1 and i%1!=0:
#         tin=i
# print(big, '-', tin, '=', round((big%1)-(tin%1), 2))

num = input('4. Введите число, которое желаете перевести в двоичное: ')
co = 0
for i in num:
# while i<len(num):
    numa=int(num)%10
    if i.isdigit:
        while int(i)%10!=0:
            # numa = int(i)%2
            i=int(i)//2
            print(i, end='')
    # num/=10
    # i+=1
