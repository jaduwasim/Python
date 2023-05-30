'''
To Display 3 employees information who are having least salary
Shell:	db.employees.find().sort({'ESAL':1}).limit(3)
Python:	empColl.find().sort('ESAL',1).limit(3)
'''

from pymongo import MongoClient
client = MongoClient()
db = client['PythonDB']
empcoll = db.employees

empCursor = empcoll.find().sort('ESAL',1).limit(3)
# print(empCursor)
# print(type(empCursor))
print('ENO\tENAME\tESAL\tEADDR')
for document in empCursor:
	print(f"{document['ENO']}\t{document['ENAME']}\t{document['ESAL']}\t{document['EADDR']}")
	# Another Way
	# print(f"{document.get('ENO')}\t{document.get('ENAME')}\t{document.get('ESAL')}\t{document.get('EADDR')}")

client.close()