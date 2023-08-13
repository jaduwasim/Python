'''
Write a python script to List out all tables in durgadb which is available in MySql Database.
'''
from pymysql import connect
con = connect(host='127.0.0.1',port=3306, database='employee', user='root',password='1234')
cursor = con.cursor()
cursor.execute('show tables')
tables = cursor.fetchall()
i=1
print(f'All Tables in Avalabale in employee')
for table in tables:
	print(f'{i}	:	{table[0]}')
	i=i+1