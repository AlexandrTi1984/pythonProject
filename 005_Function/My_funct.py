# # # # def no_paramets():
# # # #     #print('Helo world')
# # # #     return 'Helo world' # Значение которое передаем в функции. візов функции = ретерн
# # # #
# # # # #два разрів между функциями
# # # # #рекомендуется до 4-х параметров разніх
# # # # def square(num1,num2):
# # # #     return num1 ** num2
# # # #     # if num > 20:
# # # #     #     return num ** 2
# # # #     # else:
# # # #     #     return num ** 3
# # # # def print_message(name,age,prof):
# # # #     print(f'Hello {name} You are {age} old. You work is {prof}')
# # # # print_message('Alex',38,'It')
# # #
# # # #print(no_paramets())
# # # # x = square(2,4)
# # # # print(x)
# # # # print(square(10,2))
# # # # что выше функции это глобально. Внутри функции - локальные
# # # a = 1
# # # b = 2
# # # c = 3
# # #
# # # def tester (a,b,c):
# # #     a = 10
# # #     b = 20
# # #     c = 30
# # #     print(a, b, c)
# # #     return(a, b, c)
# # # print(a, b, c)
# # # x = tester(a, b, c)
# # # print(x)
# # #
# # # def test123(a, b, d,c=1): #cначала обязательніе потом по умолчанию.
# # #     return a * b * c * d
# # # print(test123(10,5,2,2)) #c идет по умолчанию
# # # print(test123(a=3, b=6, d=8,c=1)) #c идет по умолчанию
# #
# # def tester(a, b=1, *args,**kwargs):
# #     print(a, b)
# #     print(args)
# #     for arg in args:
# #         print(arg)
# #     print(kwargs)
# # tester(1, 2, 'hello', True, 23, name='Alex', age=38) #создает кортедж
#
# def sayHello():
#     print('Hello ', end='')
#
# def take_name(name):
#     sayHello() # візов из нутри функции
#     print(name)
#
# take_name("AlexTi")
#
# def wrapper (f):  #обвертка
#     print('Start work')
#     f()
#     print('End work')
#
# wrapper(sayHello)

import My_funct2    #вызов всех функций из файла функции

print(My_funct2.double(4))
print(My_funct2.triple(4))

from My_funct2 import double   #вызов одной функции
print(double(5))

