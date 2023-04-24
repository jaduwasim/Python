# wtite python script to connect with monngodb and display all databases
# Make sure first install pymongo package
# pip install pymongo
import pymongo

client = pymongo.MongoClient()
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