'''
Write a python script to Select all data from employees table of durgadb
SELECT * FROM EMPLOYEES
'''
from pymysql import connect
con = connect(host='localhost',port=3306, user='root',password='1234',database='durgadb')
cursor = con.cursor()
cursor.execute('SELECT * FROM EMPLOYEES')
all_data = cursor.fetchall()
for data in all_data:
	print(f'Eno: {data[0]} | ENAME: {data[1]} | ESAL : {data[2]} | EADDR: {data[3]}')