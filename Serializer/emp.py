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
