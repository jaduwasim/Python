class car:
	def __init__(self, name, model, color):
		self.name = name
		self.model = model
		self.color = color
	def getinfo(self):
		print(f'Car Name : {self.name}, car model is {self.model} and color is {self.color}')

class Employee:
	def __init__(self, ename , eno , car):
		self.ename = ename
		self.eno = eno
		self.car = car

	def empinfo(self):
		print(f'Employee Name: {self.ename}, Employee No : {self.eno}')
		print(f'Employee Car Information')
		self.car.getinfo()

c = car('Innova', '2.4V', 'Grey')
e = Employee('jadu',242536,c)
e.empinfo()
