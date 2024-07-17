# Add a single element
my_set = {1, 2, 3}
my_set.add(0)
print("Using Add function = ",my_set)
# Add multiple elements
my_set.update([10,0,5, 6, 7])
print("Using Update function = ",my_set)

# Remove an element
my_set = {1, 2, 3, 4, 5}
my_set.remove(4)
print("Using Remove function = ",my_set)
# Discard an element
my_set.discard(3)
print("Using discard function = ",my_set)
# Discard a non-existing element (no error)
my_set.discard(10)
print(my_set)


