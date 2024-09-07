import pandas as pd
# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [4, 5, 8, 10],

}
df = pd.DataFrame(data)
print(df)
# slicing rows by index
# Slice rows from index 1 to 2 (exclusive of 3)
print("Slicing rows by index = \n",df[1:3])
# Slicing rows and columns using integer positions
print("By rows and columns index \n",df.iloc[1:3, 0:2])
# Slice rows where column 'A' is greater than 2
print("Conditional Slicing \n",df[df['C'] > 4])
