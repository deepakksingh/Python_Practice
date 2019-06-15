class Employee:
    """Information about 
       the Employee class goes 
       here which is stored in __doc__ class attribute."""
    numOfEmployee = 0
    raiseAmount = 1.05
    def __init__(self,first,last,email,sal):
        self.fname = first
        self.last = last
        self.email = email
        self.sal = sal
        self.email = first + "." + last + "@company.com"
        Employee.numOfEmployee += 1

    def getFullName(self):
        self.fullname = self.fname + " " + self.last
        return '{} {}'.format(self.fname,self.last)

    def apply_raise(self):
        self.sal = int(self.sal*raiseAmount)

class Developer(Employee):
    raiseAmount = 1.10

    def __init__(self,first,last,email,sal,proglang):
        super().__init__(first,last,email,sal)
        self.proglang = proglang

emp1 = Developer("deepak","singh","deepak@gmail.com",1200000,"python")
emp2 = Employee("kumar","singh","kumar@gmail.com",1500000)

print(emp1.proglang)

print(Employee.numOfEmployee)

# print(emp1.__doc__)
# print(emp2.__doc__)
# print(emp1.__doc__)
