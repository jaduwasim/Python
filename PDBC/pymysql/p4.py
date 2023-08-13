'''
Write a python script to Create a table in durga db 
create table employees(eno int(5) primary key, ename varchar(40),esal double(10,2),eaddr varchar(10))
'''
from pymysql import connect 
con = connect(host='127.0.0.1',port=3306, user='root',database='durgadb',password='1234')
cursor = con.cursor()
command = 'CREATE TABLE EMPLOYEES(ENO INT(5) PRIMARY KEY, ENAME VARCHAR(46),ESAL DOUBLE(10,2),EADDR VARCHAR(10))'
cursor.execute(command)
print('Table Created in durgadb successfylly!')
cursor.close()
con.close()