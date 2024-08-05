import os
# remove
# os.remove('example.txt')
# rename
os.rename('example.txt', 'new_name.txt')
# file info
file_info = os.stat('new_name.txt')
print(file_info)

# exits file
exists = os.path.exists('example.txt')
print(exists)

# checking if file
is_file = os.path.isfile('example.txt')
print(is_file)

# checking if directory
is_dir = os.path.isdir('parent_dir')
print(is_dir)

# return name of user
user = os.getlogin()
print("Logged in as:", user)