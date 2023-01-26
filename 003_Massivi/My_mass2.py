course={'math','vizra'}
y=['one','two','one','three']
z=[4,2,7,7,23,1,-2,-1,-3]
print(list(set(y))) #делает уникальній убирает повтор
print(list(set(z))) #делает уникальній убирает повтор
course.add('Art') #добавить в список
course.update('Art') #добавить в список
#course.clear() #очиститка сета
course.update("Rus")
print(course)

set1={'math','Fizra','En',"Ru"}
set2={'math','Esp','Suomi',"Ru"}
print((set1.union(set2))) #соединение сетов\ дубликаты удаляются
print (set1.intersection(set2)) #находим совпадения в сетах общие элементы
print(set2.difference(set1)) # чем сет2 отличается от 1
print(set1.difference(set2))# чем сет1 отличается от 2

x=[1,2,3]
y=[1,2,3]
print(x==y)  #сравнение двух списоков,сетов и т.д