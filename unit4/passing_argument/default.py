# WAP in python to print the series 5 10 15 --- upto N term
# def series(n=10):
#     a = 5
#     for i in range(n):
#         print(a, end=' , ')
#         a = a + 5
#
# series()

# WAP in python to create a function that takes
# default argument as 10 to print a fibonaccii series
def fiboseries(n=10):
    a = 1
    b = 1
    print(a , ',', b , end = ',')
    for i in range(n-2):
        c = a + b
        print (c,end=',')
        a = b
        b = c
fiboseries()


