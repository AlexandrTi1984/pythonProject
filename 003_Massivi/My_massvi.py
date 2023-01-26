empty_lst=list()
print(type(empty_lst))

world='World'
# filled_lst=[124, 0.134,True,world, "Lebron is King",[1,[9,9,9,9,],7,8]]
# print(len(filled_lst))
# print(filled_lst[-1][1][1].upper)
courses=['History','math','lit','prog','math']
nums=[1,5,8,8,2,4,2]
# courses.remove('math') #удаление по значению
# print(courses)
#
# ppoped=courses.pop(0)  #удаление по индексу
# print(courses)
# print(ppoped)

courses.reverse() # разворот спсика
print(list(reversed(courses))) # разворот в обратном порядке списка и создание списка

nums.sort() #Сначала цифры большие буквы маленькие
print(nums)
