import  datetime
def tester (a,b,c):
 #   print(a, b, c)
    x=a+b+c
    return x

#Функция для 5 домашки
def my_timestamp (user_day):
    User_day=datetime.datetime.fromtimestamp(user_day)
    tdelta2 = (datetime.timedelta(weeks=2))
    return datetime.datetime.timestamp(User_day - tdelta2)
