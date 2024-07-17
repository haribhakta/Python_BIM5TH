# update tuple by reassign new tuple
# Original tuple
my_tuple = (1, 2, 3)
# Creating a new tuple with updated values
new_tuple = my_tuple[:1] + (10,) + my_tuple[2:]
print(new_tuple)  # Output: (1, 10, 3)

# Convert the tuple to a list, make the modifications, and then convert it back to a tuple.
# Original tuple
# suppose we have a tuple then change the item of tuple such as
# 2 into 10
my_tuple = (1, 2, 3)
print("Original tuple = ",my_tuple)
# Converting to a list
temp_list = list(my_tuple)
# Updating the list
temp_list[1] = 10
# Converting back to a tuple
new_tuple = tuple(temp_list)
print("Modified Tuple = ",new_tuple)  # Output: (1, 10, 3)
# Suppose we have tuple of 5 student names  and you should change
# the student name Rita into Asmita