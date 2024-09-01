import numpy as np

int_array = np.array([1, 2, 3], dtype=np.int32)
print(int_array.dtype)  # Output: int32

float_array = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print(float_array.dtype)  # Output: float64

complex_array = np.array([1+2j, 3+4j], dtype=np.complex128)
print(complex_array.dtype)  # Output: complex128

bool_array = np.array([True, False, True], dtype=np.bool_)
print(bool_array.dtype)  # Output: bool

str_array = np.array(['a', 'bc', 'def'], dtype=np.str_)
print(str_array.dtype)  # Output: <U3 (indicates a Unicode string of length 3)

object_array = np.array([1, 'a', 3.5], dtype=np.object_)
print(object_array.dtype)  # Output: object

structured_array = np.array([(1, 2.0), (3, 4.0)], dtype=[('x', np.int32), ('y', np.float32)])
print(structured_array.dtype)  # Output: [('x', '<i4'), ('y', '<f4')]

date_array = np.array(['2023-01-01', '2024-01-01'], dtype=np.datetime64)
print(date_array.dtype)  # Output: datetime64[D]

# to convert the data type
array = np.array([1, 2, 3], dtype=np.int16)
print(array.dtype)  # Output: int16
float_array = array.astype(np.float32)
print(float_array.dtype)  # Output: float32

