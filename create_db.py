import pyodbc

# Connecting client and database server using pyodbc module
db = pyodbc.connect('DRIVER={MySQL ODBC 8.0 Unicode Driver};'
                    'User=root;'
                    'Password=*********;'
                    'Server=localhost;'
                    'Database=database;'
                    )

cursor = db.cursor()


# Creating a Database
cursor.execute("CREATE DATABASE database;")


# Creating a table in the database
cursor.execute("CREATE TABLE customers (c_no int PRIMARY KEY AUTO_INCREMENT,"
               "fname varchar(15) NOT NULL,"
               "lname varchar(15),"
               "tel_no int(11) NOT NULL);"
               )
