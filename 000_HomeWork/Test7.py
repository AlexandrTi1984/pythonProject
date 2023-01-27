#1234565
#seconds = 14:6: 56:5

My_time_second = 1234565
"""
60 секунд
1 минута 60 сек    = 69 секунд
1 час - 60 минут   = 60 *60 = 3600 секунд
1 день - 24 часа   = 24*60*60 = 86 400 секунд

"""
day = int(My_time_second/86400)
print(day)
hour = int((My_time_second % 86400) / 3600)
minut = int(((My_time_second % 86400) % 3600) /60)
seconds = (((My_time_second % 86400) % 3600) % 60)

if day > 364:
    my_year = int(day/365)
    day = int(day - my_year*365)
    print(my_year,':',day, ":", hour, ':', minut, ':', seconds, sep='')
else:
    day = int(My_time_second / 86400)
    print(day, ":", hour, ':', minut, ':', seconds, sep='')


