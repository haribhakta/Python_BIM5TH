import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursor = conn.cursor()
id=int(input("Enter id to select?"))
sql = '''select * from users where id = %s'''
try:
    cursor.execute(sql,(id,))
    result=cursor.fetchall()
    for data in result:
        print(data)
except conn.error as err:
    print("Error : ",err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
