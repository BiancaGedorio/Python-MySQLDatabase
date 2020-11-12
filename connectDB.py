import mysql.connector

# connecting client and database server using mysql connector module
conn = mysql.connector.connect(host='localhost',
                               user='root',
                               password='***********',
                               database='database'
                               )

cursor = conn.cursor()

# Executing the select command. It displays all the contents in a table.
cursor.execute("Select * from customers;")
for x in cursor:
    print(x)

