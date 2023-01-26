course={'En','1Math','RU','Esp','uA','RU'} #в сете нет индекса не от сортированній.
#Сет при віводе дублированніе єлементі не выводит . исп для убирание дубликатов
# nums={1,6,5,7,8,2,3}
# print(course)
# #empty_set=set()
# course.remove('RU')
# print(course)
# x=course.pop() #удаление последнего, если строка то рандомный
# print(nums)
# x=nums.pop() #удаление последнего
# print(x)

#y=['One','Two',"Three",'One','Two']
y=[1,2,3,5,-9,3,2,-6,56]
print(list(set(y))) # записывает новый список гдебудут только уникальные значения

course.add('OOO') #добавление єлемента
print(course)
course.update(['555','6777']) #обнови такими єлементами
print(course)
course.clear()  #очищает
print(course)

set1={'En','zzz','uA','RU'}
set2={'En','tttt','RU','Esp','uuuuu'}
print(set1.union(set2)) # обьединения 2 сетов с. дубликаты убираются

print(set1.intersection(set2))  # Находит совпадения по двум сетам
print(set1.difference(set2))  # чем сет1 отличается от стеа2
print(set2.difference(set1))   # чем сет2 отличается от стеа1

#можно сравнивать сет и список () [] {}
x=[1,2,3]
y=[1,2,3]
print(x==y)

x={1,2,3}
y={1,2,3}
print(x==y)

#Конвертация
list()
tuple()
set()