import pandas as pd
# Sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)
print(df)
# Subset DataFrame with specific columns 'A' and 'C'
subset_df = df[['A', 'C']]
print("By specific columns \n",subset_df)
# Subset rows where column 'A' is greater than 2
subset_df = df[df['A'] > 2]
print("Subset by row condition \n",subset_df)
# Subset rows where column 'A' > 2 and select columns 'A' and 'C'
subset_df = df.loc[df['A'] > 2, ['A', 'C']]
print("Subset rows where condition in column \n",subset_df)
# Subset rows where column 'A' > 1 and column 'B' < 8
subset_df = df[(df['A'] > 1) & (df['B'] < 8)]
print(subset_df)

# Subset rows where column 'A' is in a given list of values
subset_df = df[df['A'].isin([1, 3])]
print("subset by column values \n",subset_df)

# Subset the first two rows and the first two columns using iloc
subset_df = df.iloc[:2, :2]
print("By using location based\n",subset_df)
# Subset rows by labels using loc (inclusive of last index)
subset_df = df.loc[1:3, 'A':'B']
print("By using location and label \n",subset_df)

# Subset rows where column 'A' is greater than 2 using query()
subset_df = df.query('A > 2')
print("Subset with query\n",subset_df)

