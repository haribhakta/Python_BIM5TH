import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursor = conn.cursor()
sql = '''
update users set email=%s where id=%s
'''
id=input("Enter id to update = ")
email=input("Enter your email =")
try:
    cursor.execute(sql,(email,id))
    conn.commit()
    print(cursor.rowcount," Rows are updated successfully.")
except conn.error as err:
    print("Error : ",err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()