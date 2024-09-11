import mysql.connector
# Establishing the connection
conn = mysql.connector.connect(
    host="localhost",      # Replace with your MySQL server host
    user="root",   # Replace with your MySQL username
    password="", # Replace with your MySQL password
    database="school"  # Replace with your MySQL database name
)
# Creating a cursor object to interact with the database
cursor = conn.cursor()
# Executing a query
cursor.execute("SELECT DATABASE();")
# Fetching the result
result = cursor.fetchone()
print("You're connected to database: ", result)
# Closing the connection
cursor.close()
conn.close()
