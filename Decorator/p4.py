def get_ready(fun):
	def inner():
		print('Hair Decorator')
		print('Face Decorator with platatinum package')
		print('fair and lovely etc')
		fun()
	return inner
@get_ready
def Now_Redy():
	print('Now I am Ready')
Now_Redy()