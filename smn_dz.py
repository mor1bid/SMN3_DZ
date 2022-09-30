# a - открытие для добавления данных; r - открытие для чтения; w - открытие для записи данных
# w+, r+
colors = ['red', 'blue', 'green']
data = open('txt.txt', 'a')
data.writelines(colors, ',')
data.close()


path = 'txt.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()