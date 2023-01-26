#Словарь тип данных
x=5
empty_dict={'name':'Alex','surname':'Ti',x:'Five', #пара ключ значение
   'lst':[1,2,3,4],'dct':{'one':1,'two':2}}
print (empty_dict)
print (empty_dict['name'])
print (empty_dict['lst'][1]) #первій єлемент их списка
print (empty_dict['dct']['one']) #возврат из словаря по ключу one
#нельзя обращаться к несуществующему ключу
print (empty_dict.get('job','Нет ключа')) # возвращает False или строку (нет ключа) если нет ключа чтоб не было ошибки.
empty_dict['name']='Beavis'
empty_dict['phone']='978' # Добавляется новый ключ и значение Если его не существовало
empty_dict.update(name='AlexTi',surname='Tii') #изменение данных словарей
empty_dict.update({'name':'AlexTi','surname':'Tii','job':'It'}) #изменение данных словарей
x=empty_dict.pop('name') #удаление в переменную
del empty_dict['surname'] #удаление ключ значение
print(x)
print(empty_dict)
print(len(empty_dict))
print(empty_dict.keys()) #ключ
print(empty_dict.values()) #значение
print(empty_dict.items()) #ключ значение

for key,val in empty_dict.items(): #т.к ключ и знач, выводим 2 знач
    print(key) # віводит ключ
    print(val) #выводит значение
    print()