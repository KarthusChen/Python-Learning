import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='windows2012',
    database='sql_tutorial')

cursor=connection.cursor()

cursor.execute("select * from `branch`;")

records=cursor.fetchall()
for r in records:
    print(r)


cursor.close()
connection.close()