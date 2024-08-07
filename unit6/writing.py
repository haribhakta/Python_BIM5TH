filename="example1.txt"
with open(filename, "w") as file:
    content = input("Enter data to save into file")
    file.write(content)
    print("Date saved")

with open(filename,"r") as file:
    content = file.read()
    print(content)

content = input("Enter content for file")
with open(filename,"a") as file:
    file.write(content)
    print("Date saved")

with open(filename,"r") as file:
    content = file.read()
    print(content)
