# Write a program in python to create a databases name PythonDB2 and in that
# Database create a collection named with employee and insert Multiple document

import pymongo
client = pymongo.MongoClient()
db = client['PythonDB']
emp_collection = db.employees
emp_list = [
{'Eno':200, 'Ename':'Sunny','Esal':2000,'Eaddr':'Mumbai'},
{'Eno':300, 'Ename':'Bunny','Esal':3000,'Eaddr':'Hyderabad'},
{'Eno':400, 'Ename':'chinny','Esal':4000,'Eaddr':'Hyderabad'},
{'Eno':500, 'Ename':'Pinny','Esal':5000,'Eaddr':'Mumbai'}
]
emp_collection.insert_many(emp_list)
print('All document Inserted Successfully')
client.close()