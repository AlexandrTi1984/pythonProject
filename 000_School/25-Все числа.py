"""
Найдите все натуральные числа, принадлежащие отрезку
[45 000 000, 50 000 000 у которых ровно пять различных нечётных делителей
 (количество чётных делителей может быть любым).
В ответе перечислите найденные числа в порядке возрастания
"""


import itertools
import math

my_counter = 0
for x in range(45000000, 50000001):
    counter = 0
    my_list = []
    for i in range(1,1000):
        #Если нечетный делитель и делимое
        if math.fmod(x, 2) > 0 and math.fmod(i, 2) > 0 and math.fmod(x,i) == 0:
            counter += 1
            my_list.append(i)
        if counter == 5:
            print(x,my_list)
            my_counter +=1
            break
    if my_counter==5:
        break



