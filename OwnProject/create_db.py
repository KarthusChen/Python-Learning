import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='windows2012')

cursor=connection.cursor()

# cursor.execute("create database `qq`;")


# cursor.execute("show databases;")
# records=cursor.fetchall()
# for r in records:
#     print(r)


cursor.execute("use `sql_tutorial`;")
cursor.execute("create table `qq` (qq INT);")


cursor.close()
connection.close()