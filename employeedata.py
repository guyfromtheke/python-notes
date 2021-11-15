

class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = first + '.' + last + '@company.com'


        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
# this raise is hidden in this method. 
# But it can also be instanciated at the top. from the class. 


emp_1= Employee('duncan', 'njoroge', 50000)
emp_2= Employee('hellen', 'njoroge', 60000)

print(emp_1.__dict__)

emp_1.raise_amount = 1.05


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

"""
print(emp_1.pay)
emp_1.apply_raise()
print(emp_2.pay)
"""


