# Python f-string for objects;
# ---------------------------
'''
str.format() method will always call str() only.
But in f-string, we can call either __str__() or __repr__() based on our requirements
'''
class Student():
	def __init__(self, name, rollno, marks):
		self.name = name
		self.rollno = rollno
		self.marks = marks

	def __str__(self):
		return f'Name:{self.name}, Roll No:{self.rollno}, Marks:{self.marks}'

	def __repr__(self):
		return f'Student Name:{self.name}, Student Roll No:{self.rollno}, Student Marks:{self.marks}'

s = Student('Ravi',101,90)
print('Infromation: {}'.format(s)) #It Will Call __str__() methot always
print(f'Infromation: {s}') # Here It will call __str__() method 
print(f'Infromation: {s!r}') # Here It wil call __repr__() method