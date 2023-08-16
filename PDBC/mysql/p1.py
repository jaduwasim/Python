# pip install mysql-connector-python
import mysql.connector
connection = mysql.connector.connect(
	host="localhost",
	user= "root",
	password="1234",
	database="employee"
	)
cursor = connection.cursor()
cursor.execute('show databases')
db = cursor.fetchall()
print(db)

connection.close()