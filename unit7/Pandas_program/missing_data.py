import pandas as pd
data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'},
    {'Name': 'Hari', 'Age': None, 'City': 'Bharatpur'},
    {'Name': 'Bikash', 'Age': 34, 'City': None}
]
df = pd.DataFrame(data)
print(df)
print("Missing Data by null = ",df.isnull())
print("Missing Data by na = ",df.isna())

print("Missing Data Summary = ",df.isnull().sum())
print("Filling Missing Values = ",df.fillna({'Age': 0, 'City': 'unknown'}))
# print("Replacing Missing Values = ",df.replace(df.NaN,0))
print("Interpolate = ",df.interpolate(method='linear'))
