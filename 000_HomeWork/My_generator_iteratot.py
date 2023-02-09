def squares (start,stop):
    for i in range(start,stop):
        yield i==2  #функция генератор. не сразу результат а поочередно
x=squares(1,11)
print(x)
print(type(x))