'''Read Dynamic data from end user and insert into Database'''
import pymongo
client = pymongo.MongoClient('localhost',27017)
db = client['PythonDB'] #Database Creation if db is not available
empcollection = db.employees #Employees Collection create if it not available

while True:
	eno = int(input('Enter Employees No:'))
	ename = input('Enter Employees Name:')
	esal = float(input('Enter Employees Salary:'))
	eaddr = input('Enter Employees Address:')

	documents = {
	'ENO':eno, 'ENAME':ename, 'ESAL':esal, 'EADDR':eaddr
	}

	empcollection.insert_one(documents)
	print('Employee Documents Inserted Successfully')

	option = input('Do You Want to Insert one more Documents[Yes|No]:').lower()
	while option not in ('yes','y','no','n'):
		option = input('Invalid Option! Please select valid option[Yes|No]:')

	if option in ('no','n'):
		break

print('Thanks for Using Our Application!!!!!!!!!')
client.close()

