import pandas as pd
# from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(df)

# from list of dictionary
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
df = pd.DataFrame(data)
print(df)


# from list
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
columns = ['Name', 'Age', 'City']
df = pd.DataFrame(data, columns=columns)
print(df)

# from numpy array
import numpy as np
data = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)

