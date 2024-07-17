# wap in python to enter a string and check whether it is
# palindrome or not
s = input("Enter a string= ")
revs = s[::-1]
if s == revs:
    print (f"{s} is palindrome")
else:
    print(f"{s} is not palindrome")
