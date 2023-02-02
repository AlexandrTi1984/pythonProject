import  datetime
import  csv
def tester (a,b,c):
 #   print(a, b, c)
    x=a+b+c
    return x

#Функция для 5 домашки
def my_timestamp (user_day):
    User_day=datetime.datetime.fromtimestamp(user_day)
    tdelta2 = (datetime.timedelta(weeks=2))
    return datetime.datetime.timestamp(User_day - tdelta2)


#Функция для 7 домашки
def my_top (pokazatel,top_count):
    print(pokazatel,top_count)
    my_list1 = []
    my_list2 = []
    with open('2019.csv', 'r', encoding='UTF8') as csv_file:
        csv_reader = list(csv.reader(csv_file))
        y = iter(csv_reader)   #перекидываем для уменьшения памяти и убираем хедер
        next(y)

        # # перекидываем в 2 списка - в одном название, в другом значение
        for line in y:
            my_list1.append(line[1])
            my_list2.append(line[pokazatel])
        print('ТОП-' + str(top_count) + ' стран')
    # вычисляем максимальное значение, находим индекс его, потом удаляем из списка
    for i in range(top_count):
        indeks = int((my_list2.index(max(my_list2))))
        print(i+1,'.',my_list1[indeks], my_list2[indeks])
        my_list1.pop(indeks)
        my_list2.pop(indeks)

def my_menu (numeric):
    print(numeric)
    if numeric == '1':
       return 4
    elif numeric == '2':
        return 5
    elif numeric == '3':
        return 6
    elif numeric == '4':
        return 7
    elif numeric == '5':
        return 8
    elif numeric == '0':
        quit()
    else:
        print('Choice is out of range!')

def my_menu2 (numeric):
    print(numeric)
    if numeric == '1':
       return 3
    elif numeric == '2':
        return 5
    elif numeric == '3':
        return 10
    elif numeric == '0':
        quit()
    else:
        return int(numeric)
