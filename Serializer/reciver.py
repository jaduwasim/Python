import pickle

f = open('emp.ser','rb')
print('Deserialization of Employee object printing')
while True:
	try:
		neobj = pickle.load(f)
		neobj.display()
	except EOFError:
		break