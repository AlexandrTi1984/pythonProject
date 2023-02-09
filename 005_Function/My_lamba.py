# def sorting(value):
#     return value[1]

x=[[1,5,1],[2,4,2],[3,6,1],[2,1,6],[2,1,0]]
print(x)
x.sort(key=lambda value:value[2])   #Лямба безимянная функция одноразовая
print(x)