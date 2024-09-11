import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursor = conn.cursor()
sql = '''
insert into users(name,email,age) values (%s, %s, %s)
'''
name=input("Enter your name=")
email=input("Enter your email=")
age=int(input("Enter your age="))
# val=[
#     ('shyam','shyam@gmail.com','22'),
#     ('rita','rita@gmail.com','27'),
#     ('hira','hira@gmail.com','28')
# ]
val=(name,email,age)
try:
    cursor.execute(sql,val)
    conn.commit()
    print(cursor.rowcount," Rows are inserted successfully.")
except conn.error as err:
    print("Error : ",err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()