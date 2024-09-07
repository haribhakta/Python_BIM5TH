import pandas as pd
# Sample DataFrames with indices
df1 = pd.DataFrame(
    {
        'Name': ['Alice', 'Bob', 'Charlie', 'David']
    },
    index=[1, 2, 3, 4]
)
df2 = pd.DataFrame(
    {
        'Score': [85, 90, 75, 88]
    },
    index=[3, 4, 5, 6]
)
# Join based on index
joined_df = df1.join(df2, how='inner')
print("Inner join\n",joined_df)

# Set 'ID' as the index and perform join
joined_df = df1.join(df2, how='left')
print("Join on left\n",joined_df)


