'''
Write a python Script to Connect with MySql Database, Where Database name : durgadb,
in Mysql durgadb shold be available.
'''

from pymysql import connect

# con = connect(host='127.0.0.1', port = 3306, database='durgadb', user='root',password='1234')
con = connect(host='localhost', port = 3306, database='durgadb', user='root',password='1234')
if con is not None:
	print(f'Python Connected With Mysql, Now You Can Communicate With Mysql')
else:
	print('Something goes Wrong!!!')