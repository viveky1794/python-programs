# attribute of class
class Employee:
#comman base class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(self.name)
        print(self.salary)

emp1 = Employee("vivek",100)

emp1.display() # before class attribut

print( hasattr(emp1, 'salary')) # Return true if 'salary' attribute exits
print( getattr(emp1, 'salary') )# Return value of 'salary' attribute
print( setattr(emp1, 'salary',200) ) # Set attribute 'salary' at 100
print( delattr(emp1, 'salary') )# Delate attribut 'salary'

emp1.display() 






