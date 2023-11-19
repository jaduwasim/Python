# wtite python script to connect with monngodb and display all databases
# Make sure first install pymongo package
# pip install pymongo
import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017, password='')
db_list = client.list_database_names()
print('The Available Database Name:')
print('*'*40)
n=1
for db in db_list:
	print(n,':',db)
	n=n+1
client.close()

print()
print('-'*40)
print()
# OR 
from pymongo import MongoClient
client = MongoClient()
print('The Available Database Name:')
print('*'*40)
n=1
for db in db_list:
	print(n,':',db)
	n=n+1
client.close()

print('#'*95)
print('All MySQL Database')
from pymysql import connect
con = connect(host='localhost',user='root',port=3306,password='1234',database='durgadb')
cursor = con.cursor()
cursor.execute('show databases')
db_list = cursor.fetchall()
i=1
for db in db_list:
	print(f'{i} : {db[0]}')
	i+=1