class car:
	def __init__(self, car_name, car_model, car_color):
		self.car_name = car_name
		self.car_model = car_model
		self.car_color = car_color

	def carinfo(self):
		print(f'Car Name : {self.car_name}, Car Model : {self.car_model} and Color : {self.car_color}')

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def eatinfo(self):
		print('Eat Biryani and drink Bear!!!!')

class Employee(Person):
	def __init__(self, name , age, eno, esal, car):
		super().__init__(name, age)
		self.eno = eno
		self.esal = esal 
		self.car = car

	def emplinfo(self):
		print(f'Employee Name {self.name}, Employee: {self.age}')
		print(f'Employee eno: {self.eno}, Employee Salary: {self.esal}')
		print(f'Employee Car info')
		self.car.carinfo()

c = car('Innova','2.5V', 'Grey')
e = Employee('jadu', 25, 802425, 70000, c)
e.emplinfo()
e.eatinfo()