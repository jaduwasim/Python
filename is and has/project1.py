class Car:
	def __init__(self, car_name, car_model, car_no):
		self.car_name = car_name
		self.car_model = car_model
		self.car_no = car_no

	def carInfo(self):
		print(f'Car Name: {self.car_no}')
		print(f'Car Model: {self.car_model}')
		print(f'Car Number: {self.car_no}')

class person:
	def __init__(self, name, age, addr):
		self.name = name
		self.age = age
		self.addr = addr
	def personInfo(self):
		print(f'Name : {self.name}')
		print(f'Age: {self.age}')
		print(f'Address: {self.addr}')


class Employee(person):
	def __init__(self, name, age, addr, eno, esal,car):
		super().__init__(name, age, addr)
		self.eno = eno
		self.esal = esal
		self.car = car
	def empInfo(self):
		self.personInfo()
		print(f'Employee Number: {self.eno}')
		print(f'Employee Salary: {self.esal}')
		print('Car carInfo:')
		self.car.carInfo()

c = Car('Innova','2.5v', 282705)
emp = Employee('Durga Parsad',45, 'Hyderabad',646504, 500000, c)
emp.empInfo()