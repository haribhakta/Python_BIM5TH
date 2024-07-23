# Program to enter and display employee record
# using class and object
class Employee:
    def __init__(self):
        self.id=None
        self.name=None
        self.salary=None
    def putdata(self):
        self.id= int(input("Employee ID = "))
        self.name = input("Employee Name = ")
        self.salary = float(input("Employee salary = "))
    def showdata(self):
        print("ID = ",self.id)
        print("Name = ", self.name)
        print("Salary = ", self.salary)


emp = Employee()
emp.putdata()
emp.showdata()