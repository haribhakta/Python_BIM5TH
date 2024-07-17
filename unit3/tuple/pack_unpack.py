# Original tuple
my_tuple = (1, 2, 3)
# Unpacking and creating a new tuple with updated values
a, b, c = my_tuple
print("Unpack = ",a,b,c)
new_tuple = (a, 10, c)
print("Pack = ",new_tuple)  # Output: (1, 10, 3)
