import datetime
class Employee:

    number_of_employees = 0
    raise_amount=1.04

    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=f'{first.lower()}.{last.lower()}@company.com'
       # self.data_reg=datetime.datetime.now()
        Employee.number_of_employees+=1

    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'

    def pay_raise(self):
        self.pay=int(self.pay*self.raise_amount)

    @classmethod # декоратор
    def set_pay_raise(cls, amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls,emp_string):
        first,last,pay = emp_string.split('-')
        return cls(first,last,int(pay))

    @staticmethod # статичный
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() ==6:
            return False
        return True

emp_str='Simom-Lebron-2700'
# print(Employee.number_of_employees)
emp1=Employee('Jack','Smith',2000)
# print(Employee.number_of_employees)
emp2=Employee('Sara','King',3000)
emp3=Employee.from_string(emp_str)
print(emp3.__dict__)


my_day=datetime.date(2023,3,3)
print(Employee.is_workday(my_day))


# print(Employee.__dict__)
# # emp1.raise_amount=1.1
# Employee.set_pay_raise(1.99)
# emp1.set_pay_raise(2.00)
# #Employee.raise_amount=1.1 #обращение к самому классу
# print(Employee.__dict__)
# #emp1.pay_raise()
# #del emp1.raise_amount
# # Employee.pay_raise(emp1)
# # emp2.pay_raise()
# print(emp1.__dict__)
# print(emp2.__dict__)
#
# # print(Employee.number_of_employees)
# # print(emp1.pay)
# # emp1.pay_raise()
# # print(emp1.pay)
# # Employee.pay_raise(emp1)
# # print(emp1.pay)
# #print(emp1.__dict__)
# # print(emp1.__dict__)
# # emp1.first='Bob'
# print(emp2.email)
# print(emp1.fullname())
#
# print(Employee.fullname(emp1))
# print(emp2.data_reg.strftime('%Y'))

# print('hello'.upper())
# print(str.upper('hello'))
















# emp1.first='Jack'
# emp1.last='Ti'
# #print(emp1.first, emp1.last)
# print(emp1.__dict__)

