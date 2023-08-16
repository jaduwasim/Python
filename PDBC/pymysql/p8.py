'''
write a python script to list out all detail of Second Higest Salary from employee_table
Which is the table of employee database.
'''
print(f'Question: {__doc__}')
from pymysql import connect
connect = connect(host='127.0.0.1',user='root',port=3306, password='1234',database='employee')
cursor = connect.cursor()
cursor.execute('SELECT * FROM EMPLOYEE_TABLE WHERE ESAL = (SELECT MAX(ESAL) FROM EMPLOYEE_TABLE WHERE ESAL < (SELECT MAX(ESAL) FROM EMPLOYEE_TABLE))')
all_data = cursor.fetchall()
for data in all_data:
	print(f'id: {data[0]}, No: {data[1]}, Name: {data[2]}, Address: {data[3]}, Salary: {data[4]}')
connect.close()
cursor.close()