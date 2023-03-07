import datetime
class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=f'{first.lower()}.{last.lower()}@company.com'
    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'
    def pay_raise(self):
        self.pay=int(self.pay*self.raise_amount)

    def __str__(self):
        return self.fullname()
    def __repr__(self):
        return f'Employ ('')'  # описіваем что делаем если вызываем ее
    def __add__(self,other):
        return self.pay+other.pay

    def __len__(self):
        return len(self.fullname())-1




emp1=Employee('Jack','King',23000)
emp2=Employee('Jhon','Wiik',23000)

print(emp1)
print(repr(emp1))

print(emp1 + emp2)
print(len(emp2))

print(int.__add__(10,23)) # сложение из класса

# d=datetime.datetime.now()
# print(str(d))
# print(repr(d))