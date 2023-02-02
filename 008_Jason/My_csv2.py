import csv
#fieldnames - подставляем название столбцов Можно использовать терминатор, дилиметр
with open('test.csv','r',encoding='UTF8') as file:
    csv_reader=csv.DictReader(file,fieldnames=['NM','DOB','Town'])  # не подходит тем у кого нет наименования
    print(csv_reader)
    for line in csv_reader:
        print(line)

    with open('test-copy.csv','w',encoding='UTF8') as wfile:
        csv_writer=csv.DictWriter(wfile,lineterminator='\n',delimiter=',',fieldnames=['NM','DOB','Town'])
        #запись хедера
        csv_writer.writeheader()
        csv_writer.writerows(csv_reader) # записать все строки
        for line in csv_reader:
            csv.writer.writerow(line) # записать построчно
