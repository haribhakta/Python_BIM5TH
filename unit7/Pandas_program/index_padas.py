import pandas as pd
# Sample DataFrame
df = pd.DataFrame({
    'Name': ['Hari', 'Ram', 'Shyam'],
    'Age': [25, 30, 35],
    'City': ['Bharatpur', 'Tandi', 'Gaindakot']
})

# 1. Basic indexing
# Access a single value using labels
print("Name of First row = ",df.loc[0, 'Name'])  # Output: 'Hari'
# Access a row using label
print("First Row = ",df.loc[0])  # Output: First row with all columns
# Access multiple columns or rows
print("Name and City of all rows = ",df.loc[:, ['Name', 'City']])  # Select all rows for Name and City

# 2. Position based indexing
# Access the first row, first column
print("First row and first column",df.iloc[0, 0])  # Output: 'Hari'
# Access the first row
print("First row=",df.iloc[0])  # Output: First row
# Access the first two rows
print("First Two Row = ",df.iloc[:2])  # Output: First two rows
# Access the first two columns
print("First two column = ",df.iloc[:, :2])  # Output: First two columns of all rows
# 3. Boolean indexing
print("Boolean Indexing = ",df[df['Age'] > 30])
# 4. setting index and access
df.set_index('Name', inplace=True)
print("Settind index = ",df.loc['Hari'])  # Now you can access rows by Name directly
# 5. Multi-level setting index
df_multi = df.set_index(['Name','City'])
print("Multiple Index = ",df_multi.loc['Hari','Bharatpur'])
