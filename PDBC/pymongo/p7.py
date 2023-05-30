'''
To find all Employees whose salary is greater than 1500
'''
import pymongo
client = pymongo.MongoClient()
db = client['PythonDB']
empColl = db.employees

empCursor = empColl.find({'ESAL':{'$gt':1500}})
print('ENO\tENAME\tESAL\tEADDR')
for document in empCursor:
	print(f"{document['ENO']}\t{document['ENAME']}\t{document['ESAL']}\t{document['EADDR']}")
	# Another Way
	# print(f"{document.get('ENO')}\t{document.get('ENAME')}\t{document.get('ESAL')}\t{document.get('EADDR')}")

client.close()