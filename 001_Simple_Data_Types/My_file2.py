name_a = float(input("Введи строку а   "))
name_b = float(input("Введи строку b   "))
name_c= float(input("Введи строку c   "))
name_p=(name_a+name_b+name_c)/2

S=(name_p*(name_p-name_a)*(name_p-name_b)*(name_p-name_c))**0.5
print('Площадь треугольника равна= ' + str(S))
