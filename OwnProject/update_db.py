import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='windows2012',
    database='sql_tutorial')

cursor=connection.cursor()

cursor.close()
connection.commit()#动到资料的时候必须加这个才会加进去
connection.close()