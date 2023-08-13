'''
Write a python script to insert data into employees table which is the table of durgadb.
INSERT INTO EMPLOYEES(ENO,ENAME,ESAL,EADDR) VALUES (...............)
'''
from pymysql import connect
con = connect(host='localhost',user='root',port=3306, database='durgadb',password='1234')
cursor = con.cursor()
sql = 'INSERT INTO EMPLOYEES(ENO,ENAME,ESAL,EADDR) VALUES (%s,%s,%s,%s)'
records = [(100, 'Sunny',1000,'Mumbai'),(200, 'Bunny',2000,'Noida'),(300, 'Chinny',3000,'Delhi'),(400, 'Dunny',1000,'Bihar'),]
cursor.executemany(sql, records)
con.commit()
print('Data Inserted Successfully!')

con.close()
cursor.close()