import  calendar

#print(calendar.month(2023,2,w=5,l=1)) # красніе расширение между символами в пробелах
#print(calendar.calendar(2023,c=3,m=6)) #вывод календаря за год, можно менять расстояния
print(calendar.weekday(2023,1,7)) # выводит день недели порядок
print(calendar.isleap(2024)) # высокосный ли год
print(calendar.leapdays(2000,2021)) #сколько вісокосніх годов біло, скобки не включаются год
print(calendar.HTMLCalendar().formatmonth(2023,1)) # віводит код строки для Html  кода на сайт