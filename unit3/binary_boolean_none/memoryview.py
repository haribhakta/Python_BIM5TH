# Using memoryview with bytes
b = b'hello'
mv = memoryview(b)
print(mv[0])  # Output: 104

# Using memoryview with bytearray
ba = bytearray(b'hello')
mv = memoryview(ba)
mv[0] = ord('H')
print(ba)  # Output: bytearray(b'Hello')

