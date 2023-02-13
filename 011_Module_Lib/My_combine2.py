import itertools

letters = ['a','b','c','d']
numbers = [0,1,2,3]
numbers2 = [4,5,4,3,2,1,0,4,4,4,5,7]
selectors=[True,False,False,True]

# res=itertools.compress(letters,selectors) #Выбирает где True
# print(list(res))
#
# # фильтр только по True
# res2=filter(lambda x: x > 2, numbers2) # возвращает если х больше 2 через фильтр
# print(list(res2))
#
# # фильтр только по False
# res2=itertools.filterfalse(lambda x: x > 2, numbers2) # возвращает если х больше 2 через фильтр
# print(list(res2))

#Если первый вернул False остальное кидает в массив (остаток)

res=itertools.dropwhile(lambda x: x > 2, numbers2)
print(list(res))

#Набирает пока не находит False
res=itertools.takewhile(lambda x: x > 2, numbers2)
print(list(res))

#склідваем список (типа арифметическая прогрессия)
res3 = itertools.accumulate(numbers2)
print(list(res3))