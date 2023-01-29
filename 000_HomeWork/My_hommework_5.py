from My_functions import my_timestamp
"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""
import datetime
# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

#sample1=datetime.datetime.strptime(sample1,'%b %d %Y %I:%M%p')

print(type(datetime.datetime.strptime(sample1,'%b %d %Y %I:%M%p')))
print(type(datetime.datetime.strptime(sample2,'%H:%M %d/%m/%y')))
print(type(datetime.datetime.strptime(sample3,'%A, %B %d, %Y')))
print(type(datetime.datetime.strptime(sample4,'%d.%m.%Y - %H:%M:%S')))
# print(sample1)
# print(sample2)
# print(sample3)
# print(sample4)

# Write a program to print yesterdays, today and tomorrow dates

My_today = datetime.date.today()
tdelta = datetime.timedelta(days=1)

print('вчера', (My_today - tdelta).strftime('%d-%m-%Y'))
print('сегодня', My_today.strftime('%d-%m-%Y'))
print('завтра', (My_today + tdelta).strftime('%d-%m-%Y'))

# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
my_date=datetime.datetime.fromtimestamp(some_day)
#print(type(my_date))
print(my_date.__format__('%d.%m.%Y'))

# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)

User_day = float(input('Введите число от 8-ми символов '))
print(float(my_timestamp(User_day)))