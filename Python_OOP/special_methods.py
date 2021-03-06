'''
https://docs.python.org/3/reference/datamodel.html#emulating-numeric-types
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

    def __repr__(self):            
        # reproduce the instance
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):               
        # change how the object are printed and displayed
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):     
        # add empoyees' salary
        return self.pay + other.pay

    def __len__(self):
        # get the length of employee's fullname
        return len(self.fullname())

emp_1 = Employee('Jeff', 'Zhao', 50000)
emp_2 = Employee('Test', 'User', 80000)

#print(emp_1)      # we can reuse this instance
#print(repr(emp_1))
#print(str(emp_1))
#print(emp_1 + emp_2)
print(len(emp_1))