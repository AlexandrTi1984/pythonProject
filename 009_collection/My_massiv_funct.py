# int_lst = [1,2,3,4,5,6,7,8,9,10]
# new_lst=[]
#
# for x in int_lst:
#     new_lst.append(x**2)
# print(new_lst)
#
# cars = [
#     {   'make' == 'Nissan',
#         'model' == 'GTR',
#         'color' =='black'
#     }
# ]
# def return_dict(x):
#     make,model,color = cars {'make'}, cars{'model'},cars{'color'}
#         return {
#             color:{
#                 'make': make,
#                 'model': model,
#             }
#         }
# new=map(return_dict,cars) # проитерировать через функция map
# for color in new:
#     print(color)

data1=[100,200,300,400,500]
data2=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
data3=[0,1,2,3,4,5,6]

my_combo=zip(data1,data2,data3) #создание пар списка
print(list(my_combo))