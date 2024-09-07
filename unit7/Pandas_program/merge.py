import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame(
    {
        'ID': [1, 2, 3, 4],
        'Name': ['Alice', 'Bob', 'Charlie', 'David']
     }
)
df2 = pd.DataFrame(
    {
        'ID': [3, 4, 5, 6],
        'Score': [85, 90, 75, 88]
    }
)
# Inner Join on 'ID' column
merged_df = pd.merge(df1, df2, how='inner', on='ID')
print("Inner Join in id\n",merged_df)

left_join_df = pd.merge(df1, df2, how='left', on='ID')
print("Left join\n",left_join_df)

right_join_df = pd.merge(df1, df2, how='right', on='ID')
print("Right join\n",right_join_df)

outer_join_df = pd.merge(df1, df2, how='outer', on='ID')
print("outer join\n",outer_join_df)
