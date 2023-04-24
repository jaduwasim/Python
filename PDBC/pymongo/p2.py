# Write a program in python to create a databases name PythonDB and in that
# Database create a collection named with employee and insert one document

import pymongo
client = pymongo.MongoClient()
db = client['PythonDB']
emp_collection = db.employees
document = {'ENO':100, 'Ename':'Durga','Esal0':1000000, 'Eaddr':'Hyderabad'}
emp_collection.insert_one(document)
print('Document Inserted')
client.close()
