# WAP to print all prime number up to 100.

for i in range(2,101):
    c = 0
    for j in range(2,i):
        if i % j == 0:
            c = c+1
            break
    if c == 0:
        print(i, end=",")
