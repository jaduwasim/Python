# pip install mysql-connector-python
from mysql.connector import connect
connection = connect(
	host="localhost",
	user= "root",
	password="1234",
	database="employee"
	)
cursor = connection.cursor()
query = input('Enter Query:')
cursor.execute(query)
db_list = cursor.fetchall()
for db in db_list:
	print(db)
connection.close()