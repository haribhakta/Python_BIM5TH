import pandas as pd
# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
})
# Get the first 5 rows (default)
print(df.head())
# Get the first 3 rows
print(df.head(3))

# Get the last 5 rows (default)
print(df.tail())
# Get the last 3 rows
print(df.tail(3))
