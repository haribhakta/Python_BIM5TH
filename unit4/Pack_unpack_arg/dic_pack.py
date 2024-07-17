# def pack_kwargs(**kwargs):
#     print(kwargs)
#
# pack_kwargs(a=1, b=2, c=3)

# WAP in python to enter name,age and salary of an employee
# and display them
def employee(**emp):
    for key, value in emp.items():
        print(key ,"=",value)

employee(name="Rajesh Khanal",age="50",salary=50000)