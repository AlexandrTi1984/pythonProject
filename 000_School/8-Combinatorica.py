"""
Все 4-буквенные слова, составленные из букв К, Л, Р, Т, записаны в
алфавитном порядке и пронумерованы.
Вот начало списка:
1.КККК
2.КККЛ
3.КККР
4.КККТ
Запишите слово, которое стоит под номером 67.
"""

import itertools
import time


letters = ['А', 'О', 'У']
my_count=1

res=itertools.product(letters, repeat=5)  #по 4 каждого или 2
for x in res:
    if my_count == 210:
        print(my_count)
        print(x)
        break
    my_count+=1

