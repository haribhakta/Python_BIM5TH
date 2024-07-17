# Define two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# Join the tuples
joined_tuple = tuple1 + tuple2
print("Using + = ",joined_tuple) #output: (1, 2, 3, 4, 5, 6)


# Define multiple tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple3 = (7, 8, 9)
# Join all the tuples
joined_tuple = sum((tuple1, tuple2, tuple3), ())
print("Using Sum function = ",joined_tuple)

