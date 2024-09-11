import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='school'
)
cursor = conn.cursor()
sql = '''
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    age INT
)
'''
try:
    cursor.execute(sql)
    conn.commit()
    print("Table created successfully.")
except conn.error as err:
    print("Error : ",err)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
