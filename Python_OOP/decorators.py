class Employee:

    def __init__(self, first, last, pay):  
        # instance variables
        self.first = first
        self.last = last
        self.pay = pay

    @property          # we can call this method as an attribute
    def email(self):  
        return '{}.{}@company.com'.format(self.first, self.last) 

    @property
    def fullname(self): 
        return '{} {}'.format(self.first, self.last)    

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Jeff', 'Zhao', 50000)

############## Test @property ###############
'''
emp_1.first = 'Jim'   # change the first name
print(emp_1.fullname, emp_1.email)
'''
############## Test setter and deleter ###############
emp_1.fullname = 'Bill Gates'
print(emp_1.fullname, emp_1.email)
del emp_1.fullname
print(emp_1.fullname, emp_1.email)

