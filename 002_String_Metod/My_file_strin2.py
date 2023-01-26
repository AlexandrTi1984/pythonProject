# a='Hello'
# b="World"
# print(a,b, "nba", 'Lebron', sep="*", end="->") # sep - какой будет пробел
# #print('Lebr \non') # \n  перенос строки
# print('that\'s')  # \это спецсимвол
s = 2000
name="Lebron"
txt='{}s salari is {}'
#txt='{1}s salari is {2}'
print(txt.format(name,s))

product="Playstation"
price=100
txt2='this {product:} cost {price:}'
print(txt2.format(product=product,price=price))
x=123.3343434
y=23.34343434
print('x is %.4f' % x) # количество нулей, формат
print(f'Hi, my name is {product}') # f как форматирование. Форматированная строка