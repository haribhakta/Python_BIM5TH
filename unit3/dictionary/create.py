# Using Curly braces:
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
print(my_dict)

# Using dict() keyword:
my_dict = dict(
    name="Alice",
    age=25,
    city="New York")
print(my_dict)
# access element of dictionary
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 25

# access through dictionay key and values
college={
    "name": "ABC",
    "program":"BIM",
    "ESTD":2000
}
for key, val in college.items():
	print(key, " - ", val)


