# pack tuple
# def pack_args(*args):
#     print(args)
#
# tuple=(1,2,3,4,5)
# pack_args(tuple)
# WAP in python to enter salary of any 10 employees and
# find the highest salary from them
def calculate_salary(*salary):
    highest = salary[0]
    for i in salary:
        if i > highest:
            highest = i
    return highest

print ("The highest Salary = ",calculate_salary(20000,40000,25000,60000,50000))

