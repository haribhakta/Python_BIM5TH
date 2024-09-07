import pandas as pd
csv_file_path="excel_file_csv.csv"
try:
    data=pd.read_csv(csv_file_path)
except FileNotFoundError:
    print("Error: CSV file not found!")
else:
    print("Data from csv \n",data)
    # print("Data information \n",data.info())
    print("Missing Values \n",data.isnull().sum())
    print("Fill missing value mean age\n",data['Age'].fillna(data['Age'].mean(),inplace=True))
    print(data)
    select_data=data[['Name','Age']][data['Age']>20]
    print("Select name and age > 20\n",select_data)
# save to csv file\
    data.to_csv('new_csv_data.csv',index=False)




