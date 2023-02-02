import csv
import sys

with open ('test.csv', 'r', encoding='UTF8') as csv_file:  # delimiter=',' єто разделитель

    #########   закаидіваем в список ###############
    csv_reader=list(csv.reader(csv_file))
    print(csv_reader)

    with open('csv-copy.csv','w',encoding='UTF8') as new_file:
        csv_writer=csv.writer(new_file,delimiter=',',lineterminator='\n') #чтоб не біло лишних переносов, по умолчанию ,
        for line in csv_reader:
            csv_writer.writerow(line)

    ######  в строку преобразовать для одного раза для чтения ############
    # csv_reader=csv.reader(csv_file)  # является итератором
    # print(csv_reader)
    # col_names=next(csv_reader) #запись названия в переменную
    # for line in csv_reader:
    #     print(line)



#     pass
#
# x=[1,2,3,4,5]
# y=iter(x)  # используется один раз итератор. Одноразовый
#
# print(sys.getsizeof(x))
# print(sys.getsizeof(y))
#
# print(y)
# print(next(y))  #печать следующего элемента
# print(type(y))
# for i in y:
#     print(i)
#
# for i in y:
#     print(i)

