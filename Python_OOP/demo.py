
class Employee:

    # class variables
    num_of_emps = 0
    raise_amount = 1.04   

    def __init__(self, first, last, pay):  # instance 'self'(always be the first argument) 
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com' 

        Employee.num_of_emps += 1

    def fullname(self):  # the regular method automatically take the instance as the first argument
        return '{} {}'.format(self.first, self.last)    

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):  # set the class as the first argument
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):     # no default first argument
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# create instances
emp_1 = Employee('Jeff', 'Zhao', 50000)
emp_2 = Employee('Test', 'User', 80000)

############ instance variable ############
#print(emp_1.fullname())  
'''
in the background, 'emp_1.fullname()' will automatically transform to 'Employee.fullname(emp_1)'
'''
#print(emp_1.__dict__)
#print(Employee.__dict__)

############ Reguler method ############
'''
emp_1.apply_raise()
print(emp_1.pay)
emp_1.raise_amount = 1.05    # change the value of a class variable for a specific instance
emp_1.apply_raise()
print(emp_1.pay)
'''
############ Class variable ############
'''
Employee.set_raise_amt(1.05)
print(emp_1.raise_amount)
'''
############ Class method ############
'''
emp_str_1 = 'Jeff-Zhao-50000'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.__dict__)
'''
############ Static method ############
'''
import datetime
date = datetime.date(2020, 9, 5)
print(Employee.is_workday(date))
date1 = datetime.date(2020, 9, 4)
print(Employee.is_workday(date1))
'''