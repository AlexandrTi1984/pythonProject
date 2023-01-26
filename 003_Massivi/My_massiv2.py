#кортедж
course=['En','1Math','RU','Esp','uA','RU']
# print(course[::-1]) # разворот списка
nums=[1,6,5,7,8,2,3]
# Как обьявит и он не меняется
# empty_tup=1,2,3,4
# empty_tup=()
empty_tup=tuple(course)
#empty_tup[0]='gg'
print(empty_tup.count('RU')) # количество РУ
#print(empty_tup.index())
#print(empty_tup[2])
print((1,2,3) + (2,5,6)) # обьединение кортеджей

# #кортркдж из одного єлемента в кругліх скобках
# one=(1,)
# print(one)