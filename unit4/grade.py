# WAP in python to find grade of a student where user enter
# his/her percentage.
def grade(p):
    if p >= 90:
        print("A+")
    elif p >= 80:
        print("A")
    elif p >= 70:
        print("B+")
    elif p >= 60:
        print("B")
    else:
        print("C")


p = float(input("Enter your percent = "))
print("Your Grade = ",grade(p))

# print("Your grade =" , end='') , grade(p)
