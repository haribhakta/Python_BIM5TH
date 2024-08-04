import os
cwd = os.getcwd()
print("Current Working  Directory = ",cwd)
print("Content =",os.listdir())
os.mkdir('new_directory')
os.rmdir('new_directory')