# import calendar
#
# print(calendar.HTMLCalendar().formatmonth(2023,1))

import time
print(time.time()) # вовзращает тайм штам

start = time.time()
#time.sleep(5) # вынужденная пауза для того чтоб пользователь что то прочитал или просмотрел
print(time.asctime()) #вывод строки в международном формате как строка
print(time.gmtime()) # По гринвичу
print(time.localtime()) # по локальному времени
print(time.localtime() [0:4] ) # по локальному времени как кортедж

stop = time.time()

print(stop - start)