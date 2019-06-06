class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def displayEmployee(self):
        print("name: ",self.name,"\nSalary: ",self.salary)


emp1 = Employee("vivek",101)
emp1.displayEmployee()

# This is example of class creation where we can add variable in below format.
# emp1 is a class object by class variable modification

emp1.name = "shiva"
emp1.salary = 151
emp1.displayEmployee()


