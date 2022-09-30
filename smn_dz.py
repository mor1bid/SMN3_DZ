# a - открытие для добавления данных (из файла); r - открытие для чтения; w - открытие для записи данных
# w+, r+
colors = ['red', 'blue', 'green']
data = open('txt.txt', 'a')
data.writelines(colors)
data.write('\nКошмары\n')
data.write('\nИнтернета\n')
data.close()


path = 'txt.txt'
data = open(path, 'r')
for line in data:
    print(line, '\n')
data.close()