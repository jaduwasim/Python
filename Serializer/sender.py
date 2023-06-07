from emp import Employee
import pickle

f = open('emp.ser', 'wb')
while True:
	eno = int(input('Enter Employee No:'))
	ename = input('Enter Employee Name:')
	esal = float(input('Enter Employee Salary:'))
	eaddr = input('Enter Employee Address:')
	emp = Employee(eno,ename,esal,eaddr)#object creation
	pickle.dump(emp,f) #Serialization
	option = input('Do you want to Enter one More Object [Yes|No]:')
	if option.lower() == 'no':
		break

print('Multiple Employee object serialized')
