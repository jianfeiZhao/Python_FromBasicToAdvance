'''
Create a new class(developer) which inheritates all the attributes and methods in Employee class
'''
class Employee:

    # class variables
    raise_amount = 1.04   

    def __init__(self, first, last, pay):  
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com' 

    def fullname(self): 
        return '{} {}'.format(self.first, self.last)    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.1        # change the raise amount

    def __init__(self, first, last, pay, prog_lang):  
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):  
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = [employees]

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Jeff', 'Zhao', 50000, 'Python')
dev_2 = Developer('David', 'Zhang', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, dev_1)

################# Change the class variable #################
'''
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
'''
################# Test manager class #################
'''
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
'''
################# Some commonly used methods #################
print(isinstance(mgr_1, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))
print(help(type(mgr_1)))