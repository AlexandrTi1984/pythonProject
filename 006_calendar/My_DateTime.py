import datetime
d = datetime.date(2023, 1, 27)  # строка, тип данных дайт там дейт. Хранит дату
#
# print(d)
# print(type(d))
#
today = datetime.date.today() #сегодняшняя дата
# #print(today.year)
print(today - d)
# print(today.weekday())   # от 1 до 6
# print(today.isoweekday()) # от 1 до 7
#
# tdelta = datetime.timedelta(days=365.25)
# print(tdelta.total_seconds())  # конвертов в секунды
# print(tdelta)
# # #tdelta = datetime.timedelta(0,0,0,0,0,12)
# # print(tdelta + today)
# import datetime
#
# # t=datetime.time(14,25,17,8) #Есть  время
# # print(t)
# # print(type(t))
# dt=datetime.datetime(2022,11,4,12,23,56) #Есть и время и дата
# # print(dt)
# # print(dt.time())
# # print(dt.date())
#
# tdelta = datetime.timedelta(days=7,hours=23,minutes=34)
# print(dt - tdelta)
#
# today = datetime.datetime.now()
# print(today)
#
# print(today.strftime('%A-%d-%Y')) #выводит фориматированные данные как в интернете
#
# dt_str='November 30, 2020 16:23'
# new_date = datetime.datetime.strptime(dt_str,'%B %d,%Y %H') # перевод в строку по таблице кодов