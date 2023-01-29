# количство повторящихся значений
list1 = [1,2,3,5,6,7,8,9,9,8,8,8]
counter ={ }
#
for num in list1:
    counter[num] = list1.count(num)
print(counter)
result = []
for x in counter.keys():
     if counter[x] == max(counter.values()):
        result.append(x)
print(result)

#найти максимум из списка
print(max(list1))
# list1= list(set(list1))
# My_max=list1[1]
# for num in list1:
#     for j in list1:
#         if list1[num] > My_max:
#             My_max=list1[num]
#
# print(My_max)

#     counter[num] = list1.count(num)
# print(counter)
# result = []
# for x in counter.keys():
#      if counter[x] == max(counter.values()):
#         result.append(x)
#print(list1)





# # count=0
# # countmax=0
# # result=[]
# for i in range(len(list1)):
#     count = list1.count(list1[i])
#     print('Количество' , list1[i] , count)





