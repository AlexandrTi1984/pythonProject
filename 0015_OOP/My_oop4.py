import datetime
class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay

    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    def fullname(self):
        return f'{self.first.capitalize()} {self.last.capitalize()}'
    def pay_raise(self):
        self.pay=int(self.pay*self.raise_amount)

    # @fullname.setattr()
    # def fullname(self,name):
    #     first,last=name.split
    #     self.first=first
    #     self.last=last





emp1=Employee('Jack','King',23000)
emp2=Employee('Jhon','Wiik',23000)

print(emp1.email)
emp1.fullname='Sara Konor'
