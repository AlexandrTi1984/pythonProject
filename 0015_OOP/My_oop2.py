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

class Developer(Employee):# Наследование
    raise_amount = 1.55
    def __init__(self,first,last,pay,prog_lang=None):
        # Employee.__init__(self,first,last,pay)
        super().__init__(first,last,pay) #метод которій берет класс о которого наследуем
        if prog_lang:
            self.prog_lang=prog_lang
        else:
            self.prog_lang=[]
class Manager(Employee):
    def __init__(self,first,last,pay,workers=None):
        super().__init__(first,last,pay)
        if workers:
            self.workers=workers
        else:
            self.workers=[]
    def add_employee(self,emp):
        if emp not in self.workers:
            self.workers.append(emp)
    def remove_eemploet(self,emp): # удаление
        if emp in self.workers:
            self.workers.remove(emp)
    # def print_workers(self):
    #     if self.workers:
    #         for emp in self.workers:
    #             print(emp.workers)
    #     else:
    #         print('Нет людей')



emp1=Employee('Jack','Smith',2000)
emp2=Employee('Sara','King',3000)

dev1=Developer('Lebron','James',10000,['Css','Java'])
man1=Manager('Luka','Doncich',3000,[emp1,dev1])
# print(dev1.__dict__)
# print(man1.workers[1].pay)
#print(dev1.fullname())

man1.add_employee(emp2)
print(man1.__dict__)
# man1.print_workers()
# man1.remove_eemploet(emp2)
# print(man1.__dict__)


print(isinstance(man1,Manager)) #является ли ман1 инстанцией Менеджер
print(issubclass(Manager,Developer))