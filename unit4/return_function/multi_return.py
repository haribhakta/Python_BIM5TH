# WAP to show the example of function that will return
# multiple value
def calculate(a, b):
    sum = a + b
    difference = a - b
    return sum, difference


a=10
b=45
s, d = calculate(a,b)
print(s)
print(d)