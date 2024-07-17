# Concatenation Operation
str1="Hello"
str2="World"
str3=str1 + " " + str2
print("Concatenation = ", str3)

# Repetition Operation
str4 = str1 * 3
print("Repetition Operation ", str4)

# indexing in string
char = str1[0]
print("index of 0 = ",char)

# slicing in string
s="Hello how are you?"
print("slicing upto 5 ",s[0:5])
print("slicing upto 5 ",s[:5])
print("slicing from 6 ",s[6:])
print("slicing from 6 to 8 ",s[6:8])

# to find length of string
print("Length = ",len(s))

# to change case of string
print(s.upper())
print(s.lower())
print(s.title())

# to search string in string
s = "I am from nepal."
print(s.find("nepal"))
contain="india" in s
print(contain)

# to replace string in string
s="hello world"
r="python"
ns=s.replace("world",r)
print("old is = ",s)
print("New is = ",ns)

# splitting string
s="Apple, Mango, Banana"
f=s.split(",")
print(f)

# joining string
join=",".join(f)
print(join)

# string formatting
name="Rajesh"
age=30
greeting=f"Hello, {name}! Your age is {age}"
print(greeting)
greeting = "Hello,{}!Your age is {}".format(name,age)
print(greeting)
greeting = "Hello, %s! Your age is %d " %(name,age)
print(greeting)

# escaping character
s="He said \n \"hello world!\""
print(s)
s="""This 
is multiline 
string"""
print(s)

