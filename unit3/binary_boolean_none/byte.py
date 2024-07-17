# Byte literals
b = b'hello'
print(b)  # Output: b'hello'
print(type(b))
# converting string into byte
s = 'hello'
b = s.encode('utf-8')
print(b)  # Output: b'hello'

b = bytes([97,65])
print(b)

a=None
b=None
print ("None check = ",a is b)



