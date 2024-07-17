# WAP to search a number whether it is in the list or not.
sn = int(input("Enter a number to search = "))
numbers = [1, 2, 4, 5]
for num in numbers:
    if num == sn:
        print("Found the item!")
        break
else:
    print("Item not found.")
