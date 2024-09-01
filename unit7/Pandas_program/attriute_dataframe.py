import pandas as pd
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
columns = ['Name', 'Age', 'City']
df = pd.DataFrame(data, columns=columns)
print(df)
print("Shape = ",df.shape)
print("Columns = ",df.columns)
print("Index = ",df.index)
print("Data type = ",df.dtypes)
print("Size = ",df.size)
print("Values = ",df.values)
print("Info = ",df.info)
print("Is Empty = ",df.empty)