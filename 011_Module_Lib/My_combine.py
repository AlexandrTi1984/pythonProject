import itertools
#counter = itertools.count()
#counter = itertools.count(start=100, step=10)
counter=itertools.repeat(2) #бесконечноые 2

# counter = itertools.cycle(['чет','Нечет']) #бесконечные значения 1 2 3, on of. Цикл светофора
# for x in range(100):
#     print(x,next(counter))

# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# result=map(lambda x,y: x**y, range(100), itertools.repeat(2)) # подставляем всегда 2
# for x in result:
#     print(x)
# result=itertools.starmap(lambda x,y: x**y, [(0,2),(1,2),(3,4)]) # подставляем из кортеджа значение в скобках одно х другое у
# for x in result:
#     print(x)
# # # x=[1,2,3,4,5,5,7]
# #
# # for i in x:
# #     print(next(counter),':',i,sep='')
#
# data=[100,220,300,49]
#
# daily_data=itertools.zip_longest(data,range(10),fillvalue=False) #чем заменить none
# print(list(daily_data))
#
# # daily_data=zip(counter,data)
# # print(list(daily_data))
# #print(list(enumerate(data)))

letters = ['a','b','c','d']
numbers = [0,1,2,3]
names = ['Lebron','Donchi4']

# res=itertools.combinations(letters,2) # порядок не имеет значения, єлемент можно использовать 1 раз
# for x in res:
#     print(x)

# порядок имеет значения, єлемент можно использовать 1 раз
# res=itertools.permutations(letters,4)
# for x in res:
#     print(x)

#Все восможные операции
#res=itertools.product(numbers, repeat=2)  #по 4 каждого или 2
# res=itertools.product(numbers,letters, repeat=1)  #по 4 каждого или 2
# for x in res:
#     print(x)

#можно комбинировать есть повторы, нет порядка
# res=itertools.combinat ions_with_replacement(numbers,4)
# for x in res:
#     print(x)

combine = itertools.chain(letters,numbers)
print(list(combine))

combine = itertools.islice({1,2,3,4,5,6,7,8},0,5,2) #не понятно для чего
print(list(combine))

