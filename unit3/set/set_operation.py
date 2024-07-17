# union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("Union set = ",union_set)

# intesection
set1 = {1, 2, 3}
set2 = {3, 4, 5}
intersection_set = set1 & set2
print("Intesection set = ",intersection_set)

# difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
difference_set = set1 - set2
print("difference set = ",difference_set)

# symmetric difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
symmetric_difference_set = set1 ^ set2
print("Symmetric Difference Set = ",symmetric_difference_set)

# membership testing
my_set = {1, 2, 3, 4, 5}
print("3 in my set = ",3 in my_set)  # Output: True
print("6 in my set = ",6 in my_set)  # Output: False

