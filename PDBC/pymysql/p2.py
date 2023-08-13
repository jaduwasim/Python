'''
Write a python script to List out all database which is available in MySql Database.
'''
from pymysql import connect
try:
	con = connect(host='127.0.0.1',port=3306, database='durgadb',user='root',password='1234')
	if con is not None:
		print('Python Connceted With MySql Database!')
		print()
except:
	print('Something goes Wrong!')
cursor = con.cursor()
cursor.execute('show databases')
db_list = cursor.fetchall()
i=1
for db in db_list:
	print(f'{i}	:	{db[0]}')
	i = i+1