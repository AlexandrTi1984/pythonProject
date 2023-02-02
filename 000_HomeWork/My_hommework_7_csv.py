import csv

my_list1=[]
my_list2=[]
with open('2019.csv', 'r', encoding='UTF8') as csv_file:
    csv_reader = list(csv.reader(csv_file))
# # перекидываем в 2 списка - в одном название, в другом значение
    for line in csv_reader:
         my_list1.append(line[1])
         my_list2.append(line[7])
    print('ТОП стран')
#вычисляем максимальное значение, находим индекс его, потом удаляем из списка
for i in range(6):
    indeks =int((my_list2.index(max(my_list2))))
    print(my_list1[indeks], my_list2[indeks])
    my_list1.pop(indeks)
    my_list2.pop(indeks)