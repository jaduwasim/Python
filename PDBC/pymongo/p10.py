'''
Display Employee information based on Take employee name by End User
'''
import pymongo
name = input('Enter Emplyee Name to get information:')

client = pymongo.MongoClient()
db = client['PythonDB']
empColl = db.employees

document = empColl.find_one({'ENAME':name})

if document is not None:
	print('Emplyoyee Information')
	print('='*40)
	print('Employee Number:',document.get('ENO'))
	print('Employee Name:',document.get('ENAME'))
	print('Employee Salary:',document.get('ESAL'))
	print('Employee Address:',document.get('EADDR'))
else:
	print(f"{name} is not available")
client.close()