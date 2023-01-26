from builtins import print

empty_lst=[]   #обьявит список пустой
empty_lst=list()   #обьявит список пустой

# world='Hellovchil'
# filled_list=[123,world,True,'Lebron',[1,2,4,5,[5,5,5]]] # можно делать список в списке. Разные типа данных  в списке
# print(len(filled_list))
# print(filled_list[-1]) # обращение к списку по индексу можно поставить шаг
# print(filled_list[-1][1]) # обращение к списку  в списке
# Методы списка добавления
course=['En','1Math','RU','Esp','uA']
# print(course[::-1]) # разворот списка
nums=[1,6,5,7,8,2,3]
# course[1]='Art'
# print(course)
# course.append('Fizika') # добавление элемент в список в конец
# #course.append(['Fizika','vizra']) # добавление списка в список в конец
# course.extend(['Ooon','nnn']) # добавляет несколько єлементов. Разбивает список на части и добавляет в конец.
# course.insert(0,'eesti') #встака в список на позицию
#
# #course.remove('En') # удаляет 1 раз. Чтоб сделать все - по циклу и по длине списка
# #course.pop()  # удаляет последний єлемент из списка
# delElement=course.pop()  # удаленный последний элемент помешаем в переменную
# delElement=course.pop(5)  # удаленный 5 элемент помешаем в переменную
# print(course)
# print(delElement) # показывает что удалено

# print(course) # печать списка
# print(course[::-1]) #рахзворот списка на єкран вівод
# print(list(reversed(course)))  # итератор в список чтоб не сохранялся список
# course.reverse()  # меняет и сохраняет оригинал
# print(course) #рахзворот списка

# course.sort(reverse=True)  # по юникоду сортировка Цифра Большие Маленькие. Сортирвка только однородніх. reverse - обратній порядок
# print(course)
print(sorted(course)) # сортировка без сохранения
# nums.sort()
# print(nums)
#
# print(min(nums))
# print(max(nums))
# print(sum(nums))
# print(course.index('En')) # индекс по значению есть старт и енд
# print(course[course.index('En')]) # віводит значение списка по индексу
# print('En' in course) # Булеан есть ли Енгдиш в списке
#
# courses_str=str(course) # конвертор в строку со свсеми скобками
# print(courses_str)
#
# courses_str='**'.join(course) # конвертор в строку c разделителем строки. Вставляем єлементі
# print(courses_str)
# new_lst=courses_str.split('**') #разделяет по разделителю в список
# print(new_lst)
#
# print(list('Lebron King')) # по буквенно делит строку на элементы списка
# print(course + nums) # сложение списка. Второй идет в конец
# print(course[2] + str(nums[3])) # вібор єлементов списка

course2=course  # будет менять и там и там
course2=course.copy() # создается копия, чтоб при внесении изменинений оригинал не менялся !!!
course2[2]="tt2"
course[3]='iii4'
# поменялись и там и там єлементі Хранятся в єлементах памяти ссілку
print(course)
print(course2)
print(id(course2))
print(id(course))
