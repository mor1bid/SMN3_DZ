si = int(input('1. Задайте длину списка: '))
ray = []
res = 0
print('Введите', si, 'элемента(-ов) списка:')
for i in range(si):
    num = int(input())
    ray.append(num)
print(ray)
for i in range(si):
    if i%2!=0:
        res += ray[i]
print('Сумма элементов данного списка =', res)

i2 = 0
ar = []
print('2. Произведение пар элементов на нечётных позициях в данном списке =', end=' ')
for i in range(si):
    if i<si/2:
        i2-=1
        res= ray[i]*ray[i2]
        ar.append(res)
print(ar)

strip = [1.1, 1.2, 3.1, 5, 10.01]
big = 0
tin = 0
print('3. Разность между максимальным и минимальным значениями данного списка =', end='')
for i in strip:
    if i%1>big:
        big=i
    elif i%1<tin:
        tin=i
print(strip, '-', big, '-', tin, '=', big-tin)
