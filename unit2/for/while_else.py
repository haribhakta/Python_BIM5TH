# WAP to check the password attempt more than 3 times.
pa = "secret"
c = 3
while c > 0:
    p = input("Enter password: ")
    if p == pa:
        print("Access granted")
        break
    else:
        c = c - 1
else:
    print("Access denied. All attempts used.")
