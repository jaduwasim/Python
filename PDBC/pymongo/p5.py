'''To Finde onlye One Documents from collection employees of PythonDB Database'''
import pymongo 
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
db = client['PythonDB']
empcoll = db.employees

document = empcoll.find_one()
# print(type(document))
# print(document)
print('from First Way:')
print('.'*40)
print('Employee Number:',document['ENO'])
print('Employee Name:',document['ENAME'])
print('Employee Salary:',document['ESAL'])
print('Employee Address:',document['EADDR'])
print()
print('from Second Way:')
print('.'*40)
print('Employee Number:',document.get('ENO'))
print('Employee Number:',document.get('ENAME'))
print('Employee Number:',document.get('ESAL'))
print('Employee Number:',document.get('EADDR'))

client.close()