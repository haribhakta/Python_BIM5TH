import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursor = conn.cursor()
sql = '''delete from users where id=%s'''
id = input("Enter id to delete = ")
try:
    cursor.execute(sql,(id,))
    conn.commit()
    print(cursor.rowcount," Rows are deleted Successfully.")
except conn.error as err:
    print("Error : ",err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
