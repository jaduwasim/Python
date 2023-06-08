'''
Object Serialization:
----------------------
The porcess of converting an object from python supported form to either file supported
or network supported form, is called Serialization

Object Deserialization:
-----------------------
The process of converting an object from file supported or network supported form to python
object supported form, is called object Desrialization

1. Object Serialization by using pickle
2. Object serialization by using json
3. Object serialization by using yaml

1. Object Serialization by using pickle:
----------------------------------------
we can perform serialization or deserialization of an object with respect to file by 
using pickle module.
it is python inbuilt module, 
pickle module contain dump() function to perform pickling:
pickle.dump(object, file)

pickle module contain load() fuction to perform unpickling or Unmarshling or Deserializaions

object pickle.load(file)
'''




import pickle

class Employee:
	def __init__(self,eno,ename,esal,eaddr):
		self.eno = eno
		self.ename = ename
		self.esal = esal
		self.eaddr = eaddr

	def display(self):
		print(f'Employee No: {self.eno}, Employee Name:{self.ename}, Employee Salary:{self.esal}, Employee Address: {self.eaddr}')

# emp = Employee(100, 'Durga', 10000, 'Hyderabad')
# with open('emp.ser','wb') as f:
# 	pickle.dump(emp, f)

# print('pickling Object is Completed')

# with open('emp.ser', 'rb') as f:
# 	newobj = pickle.load(f)

# print('Employe Data:')
# newobj.display()
