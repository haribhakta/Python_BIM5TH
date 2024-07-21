
def interest(p, t, r):
    i = float((p*t*r)/100)
    return i


p = float(input("Enter Principal Amount = "))
t = int(input("Enter Time in year = "))
r = float(input("Enter Interest Rate = "))
si = interest(p,t,r)
print ("Simple Interest = ",si)

