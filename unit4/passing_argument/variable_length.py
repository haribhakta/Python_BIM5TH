# WAP in python to find sum and average of list of numbers

def series(*num):
    s = 0
    for i in num:
        s = s + i
        
    a = s / len(num)
    print ("Sum = ",s)
    print("Average = ", a)

series(23,45,67,34,100,32,12,5)

