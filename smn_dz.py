si = int(input('1. Задайте длинну списка: '))
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
print('Сумма элементов данного массива =', res)

# ze = int(si/2)
i2 = 0
ar = []
print('2. Произведение пар элементов данного массива =')
for i in range(si):
    if i<si/2:
        i2-=1
        res= ray[i]*ray[i2]
        ar.append(res)
print(ar)
    

