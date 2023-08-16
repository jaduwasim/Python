'''
write python script to list out all table in employee database
'''
print(f'Question: {__doc__}')
from pymysql import connect
con = connect(host='localhost',user='root',port=3306,password='1234',database='employee')
cursor = con.cursor()
cursor.execute('show tables')
tables = cursor.fetchall()
i=1
for table in tables:
	print(f'{i} : {table[0]}')
	i+=1
con.close()
cursor.close()